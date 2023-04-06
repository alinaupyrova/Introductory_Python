import pandas as pd

# Загрузить данные из таблицы в DataFrame
df = pd.read_csv("zamowienia.csv", delimiter=";")

# Фильтровать заказы для продавцов из Польши в 2005 году
filtered_orders = df[(df["Kraj"] == "Polska") & (df["Data zamowienia"].str.startswith("2005"))]

# Подсчитать сумму заказов для выбранных заказов
total_orders = filtered_orders["Utarg"].sum()

# Вывести сумму заказов для выбранного периода и страны
print("sumę zamówień dla roku 2005, dla sprzedawców z Polski: ", total_orders)