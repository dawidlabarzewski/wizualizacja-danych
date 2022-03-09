i = 0
even = []

while i < 10:
    i += 1
    number = input('Podaj liczbę\n')

    try:
        number = float(number)
    except:
        continue

    if number % 2 == 0:
        even.append(number)

print(even)