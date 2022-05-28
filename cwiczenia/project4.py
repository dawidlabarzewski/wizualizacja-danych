import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


# plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'r:')
# plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'bo')
# plt.ylabel('wartości')
# plt.xlabel('indeksy')
# plt.axis([0, 6, 0, 20])
# plt.show()


# x = np.arange(0, 5.2, 0.2)

# plt.plot(x, x, 'r-', x, x**2, 'bs', x, x**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'sześcienna'])
# plt.show()

# plt.plot(x, x, 'r--', label='liniowa')
# plt.plot(x, x**2, 'bs', label='kwadratowa')
# plt.plot(x, x**3, 'g^', label='sześcienna')
# plt.xlabel('x')
# plt.ylabel('y')

# plt.legend(loc='upper left')
# plt.title('wykres trzech lini')
# plt.savefig('cwiczenia/plot2.png')
# plt.show()
# im1 = Image.open('cwiczenia/plot2.png')
# im1 = im1.convert('RGB')
# im1.save('cwiczenia/plot2.jpg')


# x = np.arange(1, 21, 1)
# y = 1/x

# plt.plot(x, y, 'r')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xticks(x)
# plt.show()


# x = np.arange(0, 10.1, 0.1)
# y = np.sin(x)

# plt.plot(x, y, 'r')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('y=sin(x)')
# plt.show()


# x1 = np.arange(0, 2.02, 0.02)
# x2 = np.arange(0, 2.02, 0.02)

# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)

# plt.subplot(2, 1, 1)
# plt.plot(x1, y1)
# plt.ylabel('sin(x)')
# plt.xlabel('x')
# plt.title('wykres sin(x)')

# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r')
# plt.ylabel('cos(x)')
# plt.xlabel('x')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()



# x1 = np.arange(0, 2.02, 0.02)
# x2 = np.arange(0, 2.02, 0.02)

# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)

# fig, axs = plt.subplots(3, 2)
# print(type(fig))
# print(type(axs))

# axs[0, 0].plot(x1, y1)
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[0, 0].set_title('wykres sin(x)')

# axs[1, 1].plot(x2, y2, 'r-')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[1, 1].set_title('wykres cos(x)')

# axs[2, 0].plot(x2, y2, 'r-')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('cos(x)')
# axs[2, 0].set_title('wykres cos(x)')

# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])

# plt.show()


# dane = {'a': np.arange(50),
#         'c': np.random.randint(0, 51, 50),
#         'd': np.random.randn(50)}

# dane['b'] = dane['a'] + 10 * np.random.randn(50)
# dane['d'] = np.abs(dane['d']) * 100

# plt.scatter(data=dane, x='a', y='b', c='c', s='d', cmap='plasma')
# print(dane['c'])
# plt.show()


# dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Populacja': [11190826, 1303171035, 207847528, 38645467],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}

# df = pd.DataFrame(dane)

# grupa = df.groupby('Kontynent');
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg('Populacja').sum())

# plt.bar(x=etykiety, height=wartosci, color=['red', 'green', 'blue'])
# plt.xlabel('Kontynent')
# plt.ylabel('Populacja na kontynentach')
# plt.show()


# x = np.random.randn(10000)
# plt.hist(x, bins=50, alpha=0.75, facecolor='g', density=True)
# plt.show()


print(np.random.randn(10))