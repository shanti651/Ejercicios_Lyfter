from actions import add_student, info_students, export_data, top_three_students, average_note, failed_students
from data import export_data

students = []
def system():
    while True:
        option = input("What do you want to do? ADD STUDENT = a\n IFORMATION ABOUT STUDENT = b\n TOP 3 = c\n AVERAGE NOTES = d\n EXPORT DATA = e\n FAIL STUDENTS = f\n EXIT = z") 
        if option == "z":
            break

        elif option == "a":
            student = add_student(students)
            students.append(student)
            
        elif option == "b":
            info_students(students)

        elif option == "c":
            average = top_three_students(students)


        elif option == "d":
            average = average_note(students)
            print(f"The average grade of all students is {average}")


        elif option == "e":
            print(students)
            export_data(students)

        elif option == "f":
            failed_students(students)


        else:
            print("Invalid option")
