import math

number = input('Podaj liczbę do obliczenia pierwiastka\n')

try:
    number = float(number)
except:
    print('Nie podano liczby')
    quit()

if number < 0:
    print('Podana liczba jest ujemna')
    quit()

sqrt = math.sqrt(number)

print(f'Pierwiastek z {number} to {sqrt}')