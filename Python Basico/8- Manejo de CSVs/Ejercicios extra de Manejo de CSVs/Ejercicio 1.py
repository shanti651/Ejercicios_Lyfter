import csv

with open("Ejercicios de Manejo de CSVs.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for row in reader:         
        for key, value in row.items():
            print(f"{key} : {value}")

with open("Ejercicios de Manejo de CSVs.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    calification = input("Input the calification you want to search: ")    
    for row in reader:   
        if row["Calification"] == calification:     
            for key, value in row.items():           
                print(f"{key} : {value}")