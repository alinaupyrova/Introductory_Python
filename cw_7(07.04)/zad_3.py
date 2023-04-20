import pandas as pd
import matplotlib.pyplot as plt

# загрузить данные z pliku Excel
data = pd.read_excel('imiona.xlsx')

# сгруппировать данные по году i płci i посчитать ilość urodzeń w każdym roku i płci
births_by_gender = data.groupby(['Rok', 'Plec']).sum()['Liczba']

# stworzyć dwa osobne wykresy liniowe - jeden dla ilości urodzeń dziewcząt, a drugi dla ilości urodzeń chłopców
births_by_gender['F'].plot(kind='line', label='Girls')
births_by_gender['M'].plot(kind='line', label='Boys')

# добавить podpisy osi i tytuł wykresu
plt.xlabel('Year')
plt.ylabel('Number of births')
plt.title('Number of births by year and gender')

# добавить legendę
plt.legend()

# показать wykres
plt.show()
