import pandas as pd
import xlrd
import openpyxl

table = pd.read_excel("imiona.xlsx")
print(table)

rok = table.loc[(table['Rok'] >= 2000) & (table['Rok'] <= 2005)]['Liczba'].sum()
print("Sum is", rok)
