divisible_by_4 = [x for x in range(0, 101) if x % 4 == 0]

divisible_by_4_text = "Liczby podzielne przez 4 w przedziale od 0 do 100: " + ", ".join(str(e) for e in divisible_by_4)

file = open('podzielne_przez_4.txt', 'w+')

file.write(divisible_by_4_text)