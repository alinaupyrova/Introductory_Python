import pandas as pd
import xlrd
import openpyxl

zamowienia = pd.read_csv("zamowienia.csv")
print(zamowienia)

a = zamowienia['Sprzedawca'].unique().tolist()
print(a)