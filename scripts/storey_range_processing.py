import numpy as np
import pandas as pd

def parse_storey_range(s):
    if pd.isna(s):
        return np.nan, np.nan, np.nan
    s = str(s).strip().upper()
    parts = s.split(" TO ")
    try:
        low = int(parts[0])
        high = int(parts[1]) if len(parts) > 1 else np.nan
    except ValueError:
        return np.nan, np.nan, np.nan
    avg = np.nanmean([low, high]) if not np.isnan(high) else low
    return low, high, avg

storey_vals = df["storey_range"].apply(parse_storey_range)
df[["storey_low", "storey_high", "storey_avg"]] = pd.DataFrame(storey_vals.tolist(), index=df.index)

def storey_band(avg):
    if np.isnan(avg): return np.nan
    if avg <= 6: return "Low"
    elif avg <= 12: return "Mid"
    else: return "High"

df["storey_band"] = df["storey_avg"].apply(storey_band)
