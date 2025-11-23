import pandas as pd

sample = pd.DataFrame({
    "town": ["CHOA CHU KANG"],
    "flat_type": ["4 ROOM"],
    "floor_area_sqm": [95],
    "age_of_flat": [20],
    "storey_avg": [10]
})

predicted_price = model.predict(sample)
print("Predicted resale price:", predicted_price[0])
