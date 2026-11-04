"""sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

total_por_upc = {}

for sale in sales:                 
    for item in sale["items"]:     
        upc = item["upc"]
        price = item["unit_price"]

        if upc in total_por_upc:
            total_por_upc[upc] = total_por_upc[upc] + price
        else:
            total_por_upc[upc] = price

print(total_por_upc)"""

"""employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

employees_by_department = {}

for employee in employees:
    department = employee["department"]

    if department in employees_by_department:
        employees_by_department[department].append({
            "name": employee["name"],
            "email": employee["email"]
        })
    else:
        employees_by_department[department] = [{
            "name": employee["name"],
            "email": employee["email"]
        }]

print(employees_by_department)"""

"""students = [
    {"name": "Ana", "email": "ana@mail.com", "grade": "10A"},
    {"name": "Luis", "email": "luis@mail.com", "grade": "10B"},
    {"name": "Sofía", "email": "sofia@mail.com", "grade": "10A"},
    {"name": "Pedro", "email": "pedro@mail.com", "grade": "11A"},
]
students_by_grade = {}
for student in students:
    grade = student["grade"]
    if grade in students_by_grade: 
        students_by_grade[grade].append({
            "name": student["name"],
            "email": student["email"],
        })
    else: students_by_grade[grade] = [{
        "name": student["name"],
        "email": student["email"]
    }]
print(students_by_grade)"""

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


