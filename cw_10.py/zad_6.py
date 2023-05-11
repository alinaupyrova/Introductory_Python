import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("imiona.xlsx")

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 4))

# wykres 1
women = df[df['Plec'] == "K"]['Liczba'].sum()
men = df[df['Plec'] == "M"]['Liczba'].sum()
axes[0].bar(['K', 'M'], [women, men], color=['pink', 'blue'])
axes[0].set_title("Liczba urodzeń (K vs M)")

# wykres 2
data_women = df[df['Plec'] == 'K'].groupby('Rok').sum()['Liczba']
data_men = df[df['Plec'] == 'M'].groupby('Rok').sum()['Liczba']
axes[1].plot(data_women.index, data_women, label='K')
axes[1].plot(data_men.index, data_men, label='M')
axes[1].set_title("Liczba urodzeń (K vs M) w czasie")

# wykres 3
data = df.groupby('Rok').sum()['Liczba']
axes[2].bar(data.index, data)
axes[2].set_title("Liczba urodzeń w sumie")

plt.show()
