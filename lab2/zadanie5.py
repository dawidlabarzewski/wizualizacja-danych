import sys

sys.stdout.write('Wzór: a^b + c\n')
sys.stdout.write('Wpisz 3 liczby całkowite oddzielone spacją\n')

numbers_line = sys.stdin.readline()

numbers = numbers_line.split(' ')

if len(numbers) != 3:
    sys.stdout.write('Podano nieprawidłową ilość liczb\n')
    quit()

for number in numbers:
    try:
        int(number)
    except:
        sys.stdout.write('Podana wartość nie jest liczbą całkowitą\n')
        quit()

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

result = a ** b + c

sys.stdout.write('Wynik: %s\n' % result)


