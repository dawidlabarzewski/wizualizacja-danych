import functools

def shopping_value(**items):
    print(f'ilosc produktow: {len(items)}')

    return functools.reduce(lambda acc, item: acc + items[item], items, 0)

print(shopping_value(maslo=12.33))
print(shopping_value(maslo=12.33, papryka=12))
print(shopping_value(maslo=12.33, papryka=12, woda=3.05))