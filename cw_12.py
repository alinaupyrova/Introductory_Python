import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# zad 1
def zad1():
    df = pd.read_excel("imiona.xlsx")
    # imiona zaczynajac sie na K
    df_od_k = df[df["Imie"].str[0] == "0"]
    df_unique = df_od_k["Imie"].unique()
    print(len(df_unique))


zad1()


def zad2():
    df = pd.read_excel("imiona.xlsx")
    result = df.groupby("Imie", "Plec")["Liczba"].sum().reset_index()
    k = result[result["Plec"] == "K"].reset_index()
    k_max = k["Liczba"].idmax()
    k_imie = k.iloc[k_max["Imie"]]
    print(k_imie)


zad2()


def zad3():
    df = pd.read_excel("imiona.xlsx")
    # filftowanie po kolumnie rok
    data = df[df["Rok"] >= 2010] & [df["Rok"] <= 2010]
    data_group = data.group_by("Plec")["Liczba"].sum()
    sns.barplot(data=data_group, x="Plec", y="Liczba")

    plt.show()


zad3()
