import numpy as np
import pandas as pd

df = df.copy()

# Parse month to datetime
df["month"] = pd.to_datetime(df["month"], errors="coerce")

# Clean text fields
text_cols = ["town", "flat_type", "street_name", "flat_model"]
for col in text_cols:
    df[col] = (
        df[col].astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.title()
    )

# Clean block (uppercase alphanumeric)
df["block"] = (
    df["block"].astype(str).str.strip().str.upper().str.replace(r"[^A-Z0-9]", "", regex=True)
)

# Numeric conversions
for col in ["floor_area_sqm", "lease_commencement_date", "resale_price"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows missing critical fields
df = df.dropna(subset=["month", "town", "flat_type", "floor_area_sqm", "resale_price"])
