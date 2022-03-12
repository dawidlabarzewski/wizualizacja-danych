products = {
    'butelka wody': 'sztuki',
    'jabłko': 'kg',
    'jajka': 'sztuki',
    'chleb': 'sztuki',
    'kielbasa': 'kg'
}

szt_products = [product for product in products if products[product] == 'sztuki']

print(szt_products)