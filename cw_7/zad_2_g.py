import pandas as pd

table = pd.read_excel("imiona.xlsx")
print(table)
suma = table.groupby('Plec')['Liczba'].sum()
print(suma)
the_most_popular_name_boy = suma.loc[table['Plec'] == "M"].idxmax()
the_most_popular_name_girl = suma.loc[table['Plec'] == "K"].idxmax()
print(the_most_popular_name_girl)
print(the_most_popular_name_boy)

