import csv

def export_data(students):
    with open("Students.csv", "a", newline="") as file:
        escritor = csv.writer(file)
        if file.tell() == 0:
            escritor.writerow(["name", "class_number", "spanish_grade", "english_grade", "socials_grade", "science_grade"])

        for student in students:
            escritor.writerow([
                student["name"],
                student["class_number"],
                student["spanish_grade"],
                student["english_grade"],
                student["socials_grade"],
                student["science_grade"]
            ])
        print("Student added")
        students.clear()

