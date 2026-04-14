name = input("Enter your name")
last_name = input("Enter your last name")
age = int(input("Enter your age"))
if (age <= 1 and age <= 2):
    print("The user is a baby")
elif (age <= 3 and age <= 11):
    print("The user is a child")
elif (age <= 12 and age <= 17):
    print("The user is a teenager")
elif (age <= 18 and age <= 29):
    print("The user is a young adult")
elif (age <= 30 and age <= 59):
    print("The user is an adult")
else:
    print("The user is a senior")