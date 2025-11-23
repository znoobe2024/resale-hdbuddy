import pandas as pd

df = df.loc[
    (df["floor_area_sqm"] > 20) & (df["floor_area_sqm"] < 200) &
    (df["resale_price"] > 50000) & (df["resale_price"] < 2000000)
].copy()

df = df.drop_duplicates()
