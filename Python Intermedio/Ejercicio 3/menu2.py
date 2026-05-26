from actions2 import Student
from data2 import export_data, import_data


def system():
    students = []
    while True:
        option = input("What do you want to do? ADD STUDENT = a\n IFORMATION ABOUT STUDENT = b\n TOP 3 = c\n AVERAGE NOTES = d\n EXPORT DATA = e\n FAIL STUDENTS = f\n IMPORT DATA = g\n EXIT = z").strip().lower()
        if option == "z":
            break

        elif option == "a":
            student = Student()
            student.ask_data()
            student.ask_grades()

            students = []

            s = Student()
            s.ask_data()
            s.ask_grades()

            students.append(s)
            
        """elif option == "b":
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
        
        elif option == "g":
            import_data(students)


        else:
            print("Invalid option")"""
