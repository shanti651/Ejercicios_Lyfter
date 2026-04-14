import csv

with open("Ejercicios de Manejo de CSVs.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    developer = input("Input the developer you want to search: ")    
    for row in reader:  

        if row["Developer"] == developer:     
            print(f"{row['Game Name']} (Clasification = {row['Calification']}, Gender = {row['Gender']})")
            
        
        