bakery = {}
total_products = 0
total_quantity = 0
while True:
    command = input()
    if command == "statistics":
        break
    product = command.split(": ")[0]
    quantity = command.split(": ")[1]
    if product not in bakery:
        bakery[product] = int(quantity)
        total_products += 1
        total_quantity += int(quantity)
    else:
        bakery[product] += int(quantity)
        total_quantity += int(quantity)

print("Products in stock:")
for key, value in bakery.items():
    print(f"- {key}: {value}")
print(f"Total products: {total_products}")
print(f"Total quantity: {total_quantity}")