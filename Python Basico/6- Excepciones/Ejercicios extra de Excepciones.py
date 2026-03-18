def name():
    while True:
        first_name = input("Whats your  name? ")
        if first_name.isdigit():
            print("Your name can not be a number")
        else: 
            return first_name
        



def age():
    while True:
        try:
            number = int(input("How old are you?? "))
            return number
        except ValueError:
            print("Invalid number") 
    

user_name = name()
number = age()

print(f"your name is {user_name} and you are {number} years old")


"""my_list = ['4', 'hola', '10', '5.2']
def switch_to_int(my_list):   
    for x in my_list:
        try: 
            number = int(x)
            print(f"'{x}' convertido a {number}")
        except ValueError:
            print(f"Cant switch this element {x}")
    return my_list

switch_to_int(my_list)"""


"""my_list = ['10', 'manzana', '5.5', '3', 'n/a']
def add_values(my_list):
    suma = 0
    for x in my_list:
        try: 
            number = float(x)
            suma = number + suma
            print(f"{number} correctly added")
        except ValueError:
            print(f"Invalid element: {x}")
    return suma


result = add_values(my_list)
print(f"the total is {result}")"""





