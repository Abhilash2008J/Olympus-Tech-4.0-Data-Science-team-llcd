import pandas as pd
pd.set_option("display.width", 250)
tr = pd.read_csv("dataset/Task2/train.csv")
te = pd.read_csv("dataset/Bonus_Task/test.csv")

for c in ["star_type", "planet_type", "water_presence", "surface_composition", "rings", "primary_hazard"]:
    print(f"\n{c}:", tr[c].value_counts(dropna=False).to_dict())
    print("  only in test:", sorted(set(te[c].dropna()) - set(tr[c].dropna()), key=str))

nums = ["mean_temp_c", "temp_range_c", "day_length_hours", "orbital_period_days", "orbital_distance_au"]
print(tr[nums].quantile([.01, .5, .9, .99, .995]).T)
for c in nums[:3]:
    print(f"\ntop 8 {c}:")
    print(tr.nlargest(8, c)[["planetId", "planet_type", c]].to_string(index=False))
