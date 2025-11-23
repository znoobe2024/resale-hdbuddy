import pandas as pd

df["year"] = df["month"].dt.year
df["age_of_flat"] = (df["year"] - df["lease_commencement_date"]).clip(lower=0)
df["price_per_sqm"] = df["resale_price"] / df["floor_area_sqm"]
