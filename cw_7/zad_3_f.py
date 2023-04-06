import pandas as pd

# Загрузить данные из таблицы в DataFrame
df = pd.read_csv("zamowienia.csv", delimiter=";")

# Фильтровать заказы для 2004 года
filtered_orders = df[df["Data zamowienia"].str.startswith("2004")]

# Подсчитать среднюю стоимость заказа для выбранных заказов
avg_order_cost = filtered_orders["Utarg"].mean()

# Вывести среднюю стоимость заказа для выбранного года
print("Średnią kwotę zamówienia w 2004 roku: ", avg_order_cost)