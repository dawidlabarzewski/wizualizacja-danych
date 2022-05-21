import pandas as pd
import matplotlib.pyplot as plt


xlsx = pd.ExcelFile('2020-e01/ceny.xlsx')
df = pd.read_excel(xlsx, header=0)

print(df.where(df['Rok'] == 2017).groupby('Rodzaje towarów i usług').mean())

df.set_index('Miesiące', inplace=True)

df.groupby('Rodzaje towarów i usług')['Wartosc'].plot(
    xlabel='Miesiąc',
    ylabel='Wartość',
    title='Wartość produktów w miesiącach'
)

plt.legend(loc='upper left')
plt.savefig('2020-e01/zadanie2.jpg')

