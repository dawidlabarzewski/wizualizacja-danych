def product_of_sequence(*numbers):
    if len(numbers) == 0:
        return 0

    product = 1

    for i in numbers:
        product *= i

    return product

print(product_of_sequence(2))
print(product_of_sequence(1, 2))
print(product_of_sequence(1, 2, 4))
print(product_of_sequence(1, 3))
print(product_of_sequence(1, 3, 9))
print(product_of_sequence(1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144))
