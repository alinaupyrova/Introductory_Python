import pandas as pd

table = pd.read_excel("imiona.xlsx")
print(table)
suma = table.groupby('Plec')['Liczba'].sum()
print(suma)