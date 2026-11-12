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