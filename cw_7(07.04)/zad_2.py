import pandas as pd
import matplotlib.pyplot as plt

# загрузить данные из файла Excel
data = pd.read_excel('imiona.xlsx')

# сгруппировать данные по полу и посчитать общее количество родившихся мальчиков и девочек
births_by_gender = data.groupby('Plec').sum()['Liczba']

# создать столбчатую диаграмму
plt.bar(births_by_gender.index, births_by_gender.values)

# добавить подписи осей и заголовок графика
plt.xlabel('Gender')
plt.ylabel('Number of births')
plt.title('Number of births by gender')

# показать график
plt.show()