def product_of_sequence(a = 1, b = 4, ile = 10):
    product = a

    for i in range(1, ile):
        a *= b
        product *= a

    return product

print(product_of_sequence(2, 20, 1))
print(product_of_sequence(1, 2, 2))
print(product_of_sequence(1, 2, 3))
print(product_of_sequence(1, 3, 2))
print(product_of_sequence(1, 3, 3))
print(product_of_sequence())