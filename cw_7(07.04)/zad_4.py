import pandas as pd
import matplotlib.pyplot as plt

# загрузить данные из файла CSV
data = pd.read_csv('zamówienia.csv', delimiter=';')

# сгруппировать данные по специалистам и посчитать количество заказов для каждого из них
orders_by_seller = data.groupby('Sprzedawca').count()['idZamowienia']

# создать график типа bar
plt.bar(orders_by_seller.index, orders_by_seller)

# добавить подписи осей и заголовок графика
plt.xlabel('Seller')
plt.ylabel('Number of orders')
plt.title('Number of orders by seller')

# повернуть подписи оси X на 45 градусов для улучшения читабельности
plt.xticks(rotation=45)

# показать график
plt.show()
