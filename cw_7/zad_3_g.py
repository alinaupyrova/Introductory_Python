
import pandas as pd

# Загрузить данные из таблицы в DataFrame
df = pd.read_csv("zamowienia.csv", delimiter=";")

# Фильтровать заказы для 2004 и 2005 годов
orders_2004 = df[df["Data zamowienia"].str.startswith("2004")]
orders_2005 = df[df["Data zamowienia"].str.startswith("2005")]

# Сохранить данные в файлы
orders_2004.to_csv("zamówienia_2004.csv", sep=";", index=False)
orders_2005.to_csv("zamówienia_2005.csv", sep=";", index=False)