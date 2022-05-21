import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('2020-e01/gastro.csv', header=0, sep=';', decimal='.')
df.set_index('Typy placówek', inplace=True)
df = df.transpose()

df = df.reset_index()
df = df.rename_axis(None, axis=1)
df = df.rename(columns={'index': 'Typy placówek'})

df.pivot('Rok', 'Typy placówek', 'Wartosc').plot(
    kind='bar',
    xlabel='Lata',
    ylabel='Wartosc',
    rot=0,
    title='Wartość placówek')
plt.show()