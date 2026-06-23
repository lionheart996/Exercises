elements = input().split()
searched_products =  input().split()
bakery_products = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = int(elements[i+1])
    bakery_products[key] = value
for product in searched_products:
    if product in bakery_products:
        print(f'We have {bakery_products[product]} of {product} left')

    else:
        print(f"Sorry, we don't have {product}")
