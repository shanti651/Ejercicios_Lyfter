from data2 import export_data

import csv
class Student:

    def __init__(
        self,
        name="",
        class_number="",
        spanish_grade=0,
        english_grade=0,
        socials_grade=0,
        science_grade=0
    ):
        self.name = name
        self.class_number = class_number
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.socials_grade = socials_grade
        self.science_grade = science_grade


    def ask_data(self):

        while True:
            name = input("Type the name of the student: ")

            if name.isdigit():
                print("The name can not be a number")
            else:
                self.name = name
                self.class_number = input("Type the class number: ")
                break

    def ask_grades(self):
        self.spanish_grade = ask_grades("spanish_grade")
        self.english_grade = ask_grades("english_grade")
        self.socials_grade = ask_grades("socials_grade")
        self.science_grade = ask_grades("science_grade")



    
def ask_grades(grade):
            while True:
                try: 
                    subject = int(input(f"Type the {grade} of the student: "))
                    if subject <= 0 or subject > 100:
                        print("Invalid grade, type it again")
                    else: 
                        break                                       
                except ValueError: 
                    print("Invalid Data")
            return subject

"""def info_students(students):
    for row in students:
        print(f"{row['name']} (Class = {row['class_number']}, Spanish_grade = {row['spanish_grade']}, English_grade = {row['english_grade']}, Spanish_grade = {row['spanish_grade']}, Socials_grade = {row['socials_grade']}, Science_grade = {row['science_grade']})")


def top_three_students(students):
    top_one = 0
    top_two = 0
    top_three = 0
    for row in students:
        average_grade = (float(row["spanish_grade"])+float(row["english_grade"])+float(row["socials_grade"])+float(row["science_grade"]))/4
            #print(average_grade)
        if average_grade > top_one:
            top_three = top_two
            top_two = top_one
            top_one = average_grade   
        elif average_grade > top_two:
            top_three = top_two
            top_two = average_grade 
        elif average_grade > top_three:
            top_three = average_grade

        
    for row in students:
        average_grade = (float(row["spanish_grade"])+float(row["english_grade"])+float(row["socials_grade"])+float(row["science_grade"]))/4
        if average_grade == top_one:
            print(f"Top 1 = {row['name']}, Average Grade is ({top_one})")
        if average_grade == top_two:
            print(f"Top 2 = {row['name']}, Average Grade is ({top_two})")
        if average_grade == top_three:
            print(f"Top 3 = {row['name']}, Average Grade is ({top_three})")



def average_note(students):
    total_grades = 0

    try:
        total_lines = len(students)

        for student in students:
            average_grade = (
                float(student["spanish_grade"]) +
                float(student["english_grade"]) +
                float(student["socials_grade"]) +
                float(student["science_grade"])
            ) / 4

            total_grades += average_grade

        total_average_grade = total_grades / total_lines
        return total_average_grade

    except ZeroDivisionError:
        print("ERROR: You must import the info")
        return 0
    

def failed_students(students):
    fail = []
    for row in students:
        if float(row["spanish_grade"]) < 70 or float(row["english_grade"]) < 70 or float(row["socials_grade"]) < 70 or float(row["science_grade"]) < 70:
            fail.append(row["name"])
            print(f"{row["name"]} is failed")

    print(fail)"""















