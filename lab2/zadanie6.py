a = input('Podaj pierwszą liczbę\n')
b = input('Podaj drugą liczbę\n')
c = input('Podaj trzecią liczbę\n')

if a > b:
    if a > c:
        print(f'Największa liczba to pierwsza: {a}')
    else:
        print(f'Największa liczba to trzecia: {c}')
else:
    if b > c:
        print(f'Największa liczba to druga: {b}')
    else:
        print(f'Największa liczba to trzecia: {c}')