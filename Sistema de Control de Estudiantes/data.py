import csv


def export_data(students):
    try:  
        with open("Students.csv", "w", newline="") as file:
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
            print("Info exported correctly")
            

    except FileNotFoundError:
        print("The file does not exit") 


def import_data(students):
    try:
        with open("Students.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for row in lector:
                students.append(row)
            print("Info imported correctly")
                
    except FileNotFoundError:
        print("The file does not exit") 