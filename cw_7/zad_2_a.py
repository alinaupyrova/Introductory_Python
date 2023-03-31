import pandas as pd
import xlrd
import openpyxl

names = pd.read_excel("imiona.xlsx")
print(names)

result = names[names['Liczba'] > 1000]
print(result)

print(names[names['Liczba'] > 1000])
