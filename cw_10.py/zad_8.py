import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("zamowienia.csv", sep=";")

sum_offers_every_person = df.groupby("Sprzedawca")["Utarg"].sum()
general_sum = df["Utarg"].sum()
plt.pie(sum_offers_every_person, autopct='%1.1f%%', labels = sum_offers_every_person.index)
plt.legend(title = "Sprzedawcy",loc="upper right")
plt.show()