import pandas as pd

df = pd.read_csv("dataset.csv")

df["text"] = df["text"].str.lower()

df.to_csv(
    "processed_dataset.csv",
    index=False
)

print("Preprocessing Complete")
print(df.head())