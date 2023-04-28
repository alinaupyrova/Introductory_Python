import pandas as pd
import matplotlib.pyplot as plt

# загрузить данные из файла Excel
data = pd.read_excel('imiona.xlsx')

# сгруппировать данные по году и посчитать общее количество родившихся детей в каждом году
births_by_year = data.groupby('Rok')['Liczba'].sum()
births_by_year = data.groupby('Rok').sum()['Liczba'] 
# создать линейный график
plt.plot(births_by_year.index, births_by_year.values)

# добавить подписи осей и заголовок графика
plt.xlabel('Year')
plt.ylabel('Number of births')
plt.title('Number of births by year')

# показать график
plt.show()
