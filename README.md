# resale-hdbuddy
Streamlit dashboard for Singapore HDB resale trends, price estimation, and RAG-powered chatbot.

🏠 Resale HDBuddy
Overview  
Resale HDBuddy is a Streamlit dashboard I built to explore resale flat data in Singapore. It combines data visualization, a price estimator, and a conversational assistant powered by Retrieval Augmented Generation (RAG). The project demonstrates how AI can be grounded in real datasets to provide stable, efficient, and affordable insights.  
As a 57 year old non techie, this project has been both challenging and rewarding. I learned not only the concepts of AI and RAG, but also how to use tools like Google Colab, GitHub, local command prompts, and Streamlit Cloud to bring everything together.  
________________________________________
Key Features  
•	Secure Login Page: Professional entry point requiring UserID and Password  
•	Resale Trends Visualization: Dual axis charts showing average prices and transaction volumes by town.  
•	Price Estimator: AI powered form that projects resale prices based on property details.  
•	HDB Assistant (Henry): A chatbot grounded in trend_data.csv and hdb_resale_clean.csv using RAG.  
•	Professional Theme: Clean layout, clear headings, and disclaimers for legal safety.  
________________________________________
Data Sources  
•	trend_data.csv: Yearly resale price and transaction trends by town.  
•	hdb_resale_clean.csv: Detailed resale flat records, including flat type, floor area, and year.  
________________________________________
Methodology Highlights  
•	Problem: Chatbot initially retrieved only 10 records, often missing towns lower in the dataset.  
•	Solution: Expanded retrieval to 50 records and added aggregation, balancing token limits with richer context.  
•	RAG Workflow: Pre retrieval (detect towns), Retrieval (fetch records), Post retrieval (summarize data).  
•	Additional Features: Resale Trend chart and Price Estimator included to complement the chatbot and demonstrate regression.  
________________________________________
How to Run Locally  
1.	Clone this repository:   
2.	git clone https://github.com/yourusername/resale-hdbuddy.git  
3.	cd resale-hdbuddy  
4.	Install dependencies:   
5.	pip install -r requirements.txt  
6.	Add your OpenAI API key as an environment variable:   
7.	export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"  
8.	Run the app:   
9.	streamlit run app.py  
________________________________________
Deployment on Streamlit Cloud  
1.	Create a Streamlit Cloud account.  
2.	Connect your GitHub repository.  
3.	Add your OpenAI API key in Secrets:   
4.	OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxx"  
5.	Deploy the app — you’ll get a public link to share.  
________________________________________
Disclaimer  
This app is for demonstration and learning purposes only. It does not represent HDB or any officers from HDB.  
