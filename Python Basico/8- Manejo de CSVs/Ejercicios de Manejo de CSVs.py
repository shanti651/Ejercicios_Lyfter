import csv

videogames_info = []

videogames_headers = (
    'name',
    'gender',
    'developer',
    'calification'
)

def info_and_save_videogames(path):
    with open(path, "a", encoding='utf-8') as file:
        game = csv.writer(file)
        game.writerow(["Game Name", "Gender", "Developer", "Calification"])
        while True:
            game_name = input("Input the name of de Videogame or 'finish' to exit: ")

            if game_name == "finish":
                break

            gender = input("Input the gender of de Videogame: ")
            developer = input("Input the developer of de Videogame: ")
            calification = input("Input the calification of de Videogame: ")

            game.writerow([game_name, gender, developer, calification])

info_and_save_videogames("Ejercicios de Manejo de CSVs.csv")


with open("Ejercicios de Manejo de CSVs.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

import csv

videogames_info = []

videogames_headers = (
    'name',
    'gender',
    'developer',
    'calification'
)

def info_and_save_videogames(path):
    with open(path, "w", encoding='utf-8') as file:
        game = csv.writer(file, delimiter="\t")
        game.writerow(["Game Name", "Gender", "Developer", "Calification"])
        while True:
            game_name = input("Input the name of de Videogame or 'finish' to exit: ")

            if game_name == "finish":
                break

            gender = input("Input the gender of de Videogame: ")
            developer = input("Input the developer of de Videogame: ")
            calification = input("Input the calification of de Videogame: ")

            game.writerow([game_name, gender, developer, calification])

info_and_save_videogames("Ejercicios de Manejo de CSVs con tabulacion.csv")


with open("Ejercicios de Manejo de CSVs con tabulacion.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)




