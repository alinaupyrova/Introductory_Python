import pandas as pd


df = pd.read_csv("zamowienia.csv", delimiter=";")


orders_by_seller = df.groupby("Sprzedawca")["idZamowienia"].nunique()


print(orders_by_seller)