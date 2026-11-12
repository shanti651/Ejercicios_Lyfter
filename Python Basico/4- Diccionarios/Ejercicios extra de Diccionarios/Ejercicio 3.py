students = [
    {"name": "Ana", "email": "ana@mail.com", "grade": "10A"},
    {"name": "Luis", "email": "luis@mail.com", "grade": "10B"},
    {"name": "Sofía", "email": "sofia@mail.com", "grade": "10A"},
    {"name": "Pedro", "email": "pedro@mail.com", "grade": "11A"},
]
students_by_grade = {}
for student in students:
    grade = student["grade"]
    if grade in students_by_grade: 
        students_by_grade[grade].append({
            "name": student["name"],
            "email": student["email"],
        })
    else: students_by_grade[grade] = [{
        "name": student["name"],
        "email": student["email"]
    }]
print(students_by_grade)