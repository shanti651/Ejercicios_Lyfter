"""name = input("Enter your name")
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
    print("The user is a senior")"""


"""import random

number = random.randint(1, 10)
correct = False

while not correct:
    attempt = int(input("Guess the number (1 to 10): "))

    if attempt == number:
        print("Correct! You guessed the number.")
        correct = True
    else:
        print("Incorrect, try again.")"""


"""number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))

if number_one >= number_two and number_one >= number_three:
    greatest = number_one
elif number_two >= number_one and number_two >= number_three:
    greatest = number_two
else:
    greatest = number_three

print("The greatest number is:", greatest)"""


grades = int(input("Enter the number of grades you want to input: "))
counter = 1
passed_grades = 0
failed_grades = 0
average_passed_grades = 0
average_failed_grades = 0
total_average_grades = 0

while counter <= grades:
    current_grade = int(input(f"Enter the grade, {counter}: "))
    if current_grade < 70:
        failed_grades = failed_grades + 1
        average_failed_grades = average_failed_grades + current_grade
    else:
        passed_grades = passed_grades + 1
        average_passed_grades = average_passed_grades + current_grade

    total_average_grades = total_average_grades + current_grade
    counter = counter + 1

if passed_grades > 0:
    average_passed_grades = average_passed_grades / passed_grades
else:
    average_of_passed_grades = 0

if failed_grades > 0:
    average_failed_grades = average_failed_grades / failed_grades
else:
    average_of_failed_grades = 0

average_of_total_grades = total_average_grades / grades

print("The student has this number of passed grades:", passed_grades)
print("This is the average of passed grades:", average_passed_grades)

print("The student has this number of failed grades:", failed_grades)
print("This is the average of failed grades:", average_failed_grades)

print("This is the total average of grades:", average_of_total_grades)








