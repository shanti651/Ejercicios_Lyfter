import json


pokemon = [
  {
    "name": {
      "english": "Pikachu"
    },
    "level": 25,
    "type": [
      "Electric"
    ],
    "base": {
      "HP": 35,
      "Attack": 55,
      "Defense": 40,
      "Sp. Attack": 50,
      "Sp. Defense": 50,
      "Speed": 90
    }
  },
  {
    "name": {
      "english": "Charmander"
    },
    "level": 15,
    "type": [
      "Fire"
    ],
    "base": {
      "HP": 39,
      "Attack": 52,
      "Defense": 43,
      "Sp. Attack": 60,
      "Sp. Defense": 50,
      "Speed": 65
    }
  },
  {
    "name": {
      "english": "Squirtle"
    },
    "level": 18,
    "type": [
      "Water"
    ],
    "base": {
      "HP": 44,
      "Attack": 48,
      "Defense": 65,
      "Sp. Attack": 50,
      "Sp. Defense": 64,
      "Speed": 43
    }
  }
]


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




