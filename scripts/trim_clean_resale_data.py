import pandas as pd

# Load your dataset (already uploaded into Colab)
df = pd.read_csv("hdb_resale_clean.csv")

# ✅ Step 1: Filter to last 5 years
latest_year = df["year"].max()
df_recent = df[df["year"] >= latest_year - 4]   # last 5 years including latest

# ✅ Step 2: Filter to towns 'Choa Chu Kang' and 'Bedok'
df_filtered = df_recent[df_recent["town"].isin(["Choa Chu Kang", "Bedok"])]

# ✅ Step 3: Save the trimmed dataset
df_filtered.to_csv("hdb_resale_clean_trimmed.csv", index=False)

print("Trimmed dataset saved as hdb_resale_clean_trimmed.csv")
print("Original size:", len(df), "rows")
print("Trimmed size:", len(df_filtered), "rows")
