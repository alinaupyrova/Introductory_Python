import pandas as pd
import xlrd
import openpyxl

names = pd.read_excel("imiona.xlsx")
print(names)

print(names[names['Imie'] == "Alina"])