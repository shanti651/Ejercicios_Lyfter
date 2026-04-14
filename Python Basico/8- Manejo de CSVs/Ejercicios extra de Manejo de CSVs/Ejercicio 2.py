import csv

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
