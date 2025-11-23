import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import re
import os
from openai import OpenAI

# --- Load datasets ---
trend_data = pd.read_csv("data/trend_data.csv")
resale_data = pd.read_csv("data/hdb_resale_clean.csv")

# --- Initialize OpenAI client ---
# Key is hidden from the public but still usable by your app
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# --- Page Config ---
st.set_page_config(
    page_title="Resale HDBuddy",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🏠"
)

# --- Custom CSS for professional theme ---
st.markdown("""
    <style>
        body { background-color: #f9f9f9; }
        h1 { color: #2c3e50; font-size: 28px; font-weight: 600; }
        h2 { color: #34495e; font-size: 22px; font-weight: 500; }
        .description { font-size: 14px; color: #555; margin-bottom: 10px; }
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: 15%;
        }
        .disclaimer {
            font-size: 11px;
            color: #777;
            margin-top: 20px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- Authentication State ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- Login Page ---
if not st.session_state.authenticated:
    st.markdown("<div class='centered'>", unsafe_allow_html=True)
    st.markdown("<h2>Welcome to Resale HDBuddy Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("<p>Please enter your User ID and Password to continue.</p>", unsafe_allow_html=True)

    user_id = st.text_input("User ID", key="login_userid")
    password = st.text_input("Password", type="password", key="login_password")
    login_btn = st.button("Login")

    if login_btn:
        if user_id == "3064529K" and password == "Ge0r3eOu$":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid UserID or Password")

    st.markdown(
        "<p class='disclaimer'>This site is meant for demonstration and learning purposes only. "
        "It does not represent HDB or any officers from HDB.</p>",
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# --- Dashboard (only visible after login) ---
else:
    # --- Title ---
    st.title("🏠 Resale HDBuddy")

    # ============================================================
    # SECTION 1 & 2: Side-by-side Layout (Equal Size)
    # ============================================================
    col1, col2 = st.columns(2)

    # --- Left Column: Resale Trends ---
    with col1:
        st.header("📊 Resale Trends")
        st.markdown('<p class="description">Visualize average resale prices and transactions by town. Source: trend_data.csv</p>', unsafe_allow_html=True)

        towns = trend_data['town'].unique().tolist()
        default_town = "BEDOK" if "BEDOK" in towns else towns[0]
        selected_towns = st.multiselect("Select towns:", towns, default=[default_town])

        if selected_towns:
            fig, ax1 = plt.subplots(figsize=(6,5))

            # Left axis: Average resale price
            for town in selected_towns:
                town_data = trend_data[trend_data['town'] == town]
                ax1.plot(town_data['year'], town_data['resale_price'],
                         marker="o", linewidth=2, label=f"{town} Price")
            ax1.set_ylabel("Average Price (SGD)", color="blue")

            # Right axis: Transactions
            ax2 = ax1.twinx()
            for town in selected_towns:
                town_data = trend_data[trend_data['town'] == town]
                ax2.plot(town_data['year'], town_data['transactions'],
                         linestyle="--", linewidth=2, marker="s", label=f"{town} Transactions")
            ax2.set_ylabel("Transactions", color="red")

            # Legend directly below chart
            fig.legend(loc="upper center", bbox_to_anchor=(0.5, -0.05), fontsize=9, ncol=2)
            st.pyplot(fig)

    # --- Right Column: Price Estimator ---
    with col2:
        st.header("💰 Price Estimator")
        st.markdown('<p class="description">Enter property details to get a predicted resale price. Powered by ChatGPT.</p>', unsafe_allow_html=True)

        with st.form("price_estimator"):
            town_input = st.selectbox("Town:", towns, index=towns.index(default_town))
            flat_type_input = st.selectbox("Flat Type:", resale_data['flat_type'].unique())
            floor_area_input = st.number_input("Floor Area (sqm):", min_value=30, max_value=200, step=1, value=90)
            year_input = st.selectbox("Year:", sorted(trend_data['year'].unique()))

            submit_button = st.form_submit_button("Get Price Estimate")

        if submit_button:
            context = f"""
            Town: {town_input}
            Flat Type: {flat_type_input}
            Floor Area: {floor_area_input} sqm
            Year: {year_input}
            """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an assistant that estimates HDB resale prices using provided data."},
                    {"role": "user", "content": "Based on the following inputs, give a price estimate:\n" + context}
                ]
            )

            st.success("Estimated Price:")
            st.write(response.choices[0].message.content)

    # ============================================================
    # SECTION 3: HDB Assistant Chat (Henry with Hybrid RAG)
    # ============================================================
    st.header("🤖 HDB Assistant")
    st.markdown('<p class="description">Ask Henry about resale trends. Answers are grounded in trend_data.csv and hdb_resale_clean.csv, powered by ChatGPT.</p>', unsafe_allow_html=True)

    user_question = st.text_input("Type your question:")

    if user_question:
        towns_all = trend_data['town'].unique().tolist()
        mentioned_towns = [t for t in towns_all if re.search(t, user_question, re.IGNORECASE)]

        if mentioned_towns:
            subset_trend = trend_data[trend_data['town'].isin(mentioned_towns)].head(50)
            subset_resale = resale_data[resale_data['town'].isin(mentioned_towns)].head(50)

            trend_summary = subset_trend.groupby("year")[["resale_price","transactions"]].mean().reset_index()
            resale_summary = subset_resale.groupby(["flat_type","year"])["resale_price"].mean().reset_index()

            context_trend = trend_summary.to_dict()
            context_resale = resale_summary.to_dict()
        else:
            context_trend = trend_data.head(10).to_dict()
            context_resale = resale_data.head(10).to_dict()

        context = f"""
        Trend data summary: {context_trend}
        Resale data summary: {context_resale}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Henry, an assistant that explains HDB resale trends using the provided data."},
                {"role": "user", "content": context + "\nQuestion: " + user_question}
            ]
        )

        st.write("Henry says:")
        st.write(response.choices[0].message.content)

