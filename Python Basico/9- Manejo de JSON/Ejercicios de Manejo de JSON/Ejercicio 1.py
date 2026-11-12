import json


with open("pokemones.json", "r") as archivo:
    pokemones = json.load(archivo)

name = input("Type the name: ")
level = int(input("Level: "))
type = input("Type: ")

hp = int(input("HP: "))
attack = int(input("Attack: "))
defense = int(input("Defense: "))
sp_attack = int(input("Sp Attack: "))
sp_defense = int(input("Sp Defense: "))
speed = int(input("Speed: "))

nuevo_pokemon = {
    "name": {
        "english": name
    },
    "level": level,
    "type": [type],
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
}

pokemones.append(nuevo_pokemon)

with open("pokemones.json", "w") as archivo:
    json.dump(pokemones, archivo, indent=2)




