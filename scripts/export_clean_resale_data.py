# Choose useful columns to keep
df_clean = df[[
    "month", "year", "town", "flat_type", "block", "street_name",
    "storey_range", "storey_low", "storey_high", "storey_avg", "storey_band",
    "floor_area_sqm", "flat_model", "lease_commencement_date",
    "age_of_flat", "resale_price", "price_per_sqm"
]].copy()

df_clean.to_csv("hdb_resale_clean.csv", index=False)
print(f"Saved cleaned dataset with {len(df_clean)} rows.")

from google.colab import files
files.download("hdb_resale_clean.csv")
