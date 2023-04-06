import pandas as pd
df = pd.read_csv("zamowienia.csv", delimiter=";")
unique_sellers = df["Sprzedawca"].unique()
print(unique_sellers)
