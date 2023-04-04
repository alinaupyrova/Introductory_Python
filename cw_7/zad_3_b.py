import pandas as pd
import xlrd
import openpyxl

df = pd.read_csv("zamowienia.csv")
print(df)

b = df.nlargest(5, "Utarg")
print(b[["Data zamowienia", "Utarg"]])