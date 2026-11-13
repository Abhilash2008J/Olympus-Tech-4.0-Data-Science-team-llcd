import pandas as pd
pd.set_option("display.max_columns", None, "display.width", 250)

df = pd.read_csv("dataset/Task2/train.csv")
print(df.head(3).T)
print(df.describe().T)
print("duplicate rows:", df.duplicated().sum(), "| duplicate planetId:", df.planetId.duplicated().sum())
for c in df.select_dtypes(exclude="number"):
    vc = df[c].value_counts(dropna=False)
    print(f"\n{c} ({len(vc)} unique)")
    print(vc.head(15).to_string())
