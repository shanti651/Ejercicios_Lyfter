"""hotel = {
    "name": "Hotel California",
    "stars": 5,
    "rooms": [{
        "number": 1,
        "floor": 1,
        "price_per_night": 50000
    },
    {
        "number": 2,
        "floor": 2,
        "price_per_night": 60000,
    },
    {
        "number": 3,
        "floor": 3,
        "price_per_night": 100000,
    },
    ]
}

print(hotel["rooms"])"""

"""keys = ["name", "age", "city"]
values = ["Santi", 28, "Medellin"]

dictionary = {}

for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print(dictionary)"""

list_of_keys = ["access_level", "age"]

employee = {
    "name": "John",
    "email": "john@ecorp.com",
    "access_level": 5,
    "age": 28
}

for key in list_of_keys:
    employee.pop(key, None)

print(employee)
