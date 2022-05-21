##%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# s = pd.Series([1, 3, 5, 5.5, 'a'])
# print(s)
s = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c', 'd'])
# print(s)

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190826, 1303171035, 207847528]}

df = pd.DataFrame(data)
# print(df)

# daty = pd.date_range('20220507', periods=5)
# df2 = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df2)

# df3 = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df3)

# xlsx = pd.ExcelFile('datasets/imiona.xlsx')
# df4 = pd.read_excel(xlsx, header=0)
# print(df4)

# df3.to_csv('datasets/dane2.csv', index=False)
# df4.to_excel('datasets/imiona2.xlsx', sheet_name='dane')

# print(df4.head(10))
# print(df4.tail(10))

# print(df4.sample(5))

# print(df.sample(4, replace=True))

# print(s['a'])
# print(s.a)

# print(df[0:1])
# print(df['Kraj'])
# print(df.Kraj)

# print(df.iloc[[0], [0]])
# print(df.loc[[0], 'Kraj'])
# print(df.at[0, 'Kraj'])

# print(s['a'])
# print(s[s > 10])
# print(s[(s < 13) & (s > 8)])

# print(s.where(s > 10, 'warunek niespełniony'))
# s.where(s > 10, 'warunek niespełniony', inplace=True)
# print(s)

# print(df['Kraj'])
# print(df[df['Populacja'] > 12e7])

# df['full'] = df['Kraj'] + ' ' + df['Stolica']

# s['e'] = 14
# print(s)

df.loc[3] = 'nowy element'
df.loc[4] = ['Polska', 'Warszawa', 38675467]
# print(df)

# new = df.drop([3])
# print(new)

df.drop([3], inplace=True)
# print(df)

df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
# print(df)

df.sort_values(by='Populacja', ascending=False, inplace=True)
print(df)

# grupa = df.groupby(by='Kontynent')
# print(grupa)
# print(grupa.get_group('Europa'))

grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
print(grupa)

# grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Populacja w mld', rot=0, title='Populacja na kontynentach')

# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.set_title('Populacja na kontynentach')
# plt.savefig('plot2.png')
# plt.show()

# grupa = df3.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})
# print(grupa)
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
#            fontsize=20, figsize=(8, 8), colors=['red', 'green'])
# plt.legend(loc='upper left')
# plt.show()

# seria = pd.Series(np.random.randn(1000))
# seria = seria.cumsum()

# seria.plot()
# plt.show()