import pandas as pd

table = pd.read_excel("imiona.xlsx")
year = 2010
filtered_table = table[table['Rok'] == year]
grouped_table = filtered_table.groupby(['Plec', 'Imie'])['Liczba'].sum()
the_most_popular_name_boy = grouped_table.loc['M'].idxmax()
the_most_popular_name_girl = grouped_table.loc['K'].idxmax()
print(the_most_popular_name_girl)
print(the_most_popular_name_boy)