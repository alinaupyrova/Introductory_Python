import pandas as pd

# Загрузить данные из таблицы в DataFrame
df = pd.read_csv("zamowienia.csv", delimiter=";")

# Подсчитать сумму заказов для каждой страны
total_orders_by_country = df.groupby("Kraj")["Utarg"].sum()

# Вывести сумму заказов для каждой страны
print(total_orders_by_country)