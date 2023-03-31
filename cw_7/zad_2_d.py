import pandas as pd
import xlrd
import openpyxl

names = pd.read_excel("imiona.xlsx")
print(names)

suma = names.groupby('Rok')["Liczba"].sum()
print(suma)