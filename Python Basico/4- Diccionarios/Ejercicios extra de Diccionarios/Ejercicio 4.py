products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
total_by_category = {}

for product in products:
    category = product["category"]
    price = product["price"]

    if category in total_by_category:
        total_by_category[category] = total_by_category[category] + price
    else:
        total_by_category[category] = price

print(total_by_category)
