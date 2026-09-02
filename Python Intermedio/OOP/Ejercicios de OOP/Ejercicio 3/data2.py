import csv
from actions2 import Student

def export_data(students):

    try:
        with open("Students.csv", "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "name",
                "class_number",
                "spanish_grade",
                "english_grade",
                "socials_grade",
                "science_grade"
            ])

            for student in students:
                writer.writerow([
                    student.name,
                    student.class_number,
                    student.spanish_grade,
                    student.english_grade,
                    student.socials_grade,
                    student.science_grade
                ])

        print("Info exported correctly")

    except Exception as e:
        print("Error:", e)

def import_data(students):

    try:
        with open("Students.csv", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                student = Student(
                    row["name"],
                    row["class_number"],
                    float(row["spanish_grade"]),
                    float(row["english_grade"]),
                    float(row["socials_grade"]),
                    float(row["science_grade"])
                )

                students.append(student)

        print("Info imported correctly")

    except FileNotFoundError:
        print("The file does not exist")