number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))

if number_one >= number_two and number_one >= number_three:
    greatest = number_one
elif number_two >= number_one and number_two >= number_three:
    greatest = number_two
else:
    greatest = number_three

print("The greatest number is:", greatest)