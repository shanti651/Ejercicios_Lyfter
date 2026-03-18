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


generos = {}
with open("Ejercicios de Manejo de CSVs.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        genero = row["Gender"]
        if genero in generos:
            generos[genero] += 1
        else:
            generos[genero] = 1

print("Géneros encontrados:")
for genero, cantidad in generos.items():
    print(f"{genero}: {cantidad}")


with open("Ejercicios de Manejo de CSVs.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    developer = input("Input the developer you want to search: ")    
    for row in reader:  

        if row["Developer"] == developer:     
            print(f"{row['Game Name']} (Clasification = {row['Calification']}, Gender = {row['Gender']})")
            
        
        
