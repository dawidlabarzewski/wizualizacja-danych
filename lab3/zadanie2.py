import random

lista1 = [];

for i in range(0, 10):
    lista1.append(random.randint(0, 30))

lista2 = [x for x in lista1 if x % 2 == 0]

print(lista1)
print(lista2)