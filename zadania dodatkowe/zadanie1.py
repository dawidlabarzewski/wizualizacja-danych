import math


def is_palindrome(num):
    if num < 0:
        return False

    digits = int(math.log10(n)) + 1

    for i in range(0, digits // 2):
        a = num // (10 ** i) % 10
        b = num // (10 ** (digits - i - 1)) % 10
        if a != b:
            return False

    return True


n = input('Podaj liczbę\n')
n = int(n)

is_n = is_palindrome(n)

print('liczba {} {}jest palindromem\n'.format(n, ('nie ' if is_n is False else '')))

