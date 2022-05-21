import pandas as pd
import matplotlib.pyplot as plt


values = [21, 27, 33, 15, 35]
indexes = ['A', 'B', 'C', 'D', 'E']

s = pd.Series(values, index=indexes)

s.plot( kind='pie',
        fontsize=12,
        figsize=(6, 6),
        colors=['#d82647', '#2af6ea', '#af768a', '#a2d1ef', '#7c1b53'],
        title='Tytuł',
        ylabel='',
        labels=values,
        counterclock=True,
        startangle=90)

plt.legend(loc='upper left', labels=indexes)
plt.savefig('./zadanie1.pdf')