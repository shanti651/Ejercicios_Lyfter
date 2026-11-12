"""price = int(input("Enter the product price"))
discount = 0
if (price < 100):
    discount = price * 0.02
    price = price - discount
else:
    discount = price * 0.10
    price = price - discount

print(f"The discount is {discount}")
print(f"The final price is {price}")"""

seconds = int(input("Enter the time in seconds "))
objective = 0
if (seconds < 600):
    objective = 600 - seconds
    print(f"{objective} seconds are missing to reach 10 minutes")
elif (seconds > 600):
    print("Greater")
elif (seconds == 600):
    print("Equal")

"""number = int(input("Enter a number"))
counter = 1
sum_result = 0
result = 0
while (counter <= number):
    sum_result = sum_result + counter
    counter = counter + 1

print(f"The result of the sum is {sum_result}")"""

"""celsius = int(input("Enter the temperature in Celsius degrees"))
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15
print(f"The temperature in Fahrenheit is {fahrenheit}")
print(f"The temperature in Kelvin is {kelvin}")"""

"""number = int(input("Enter a number"))
counter = 1
multiplication = 0
while (counter <= 12):
    multiplication = number * counter
    print(f"{number} x {counter} = {multiplication}")
    counter = counter + 1"""

