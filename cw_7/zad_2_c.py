import pandas as pd
import xlrd
import openpyxl

names = pd.read_excel("imiona.xlsx")
print(names)
suma = names["Liczba"].sum()
print("Sum of all children is", suma)
