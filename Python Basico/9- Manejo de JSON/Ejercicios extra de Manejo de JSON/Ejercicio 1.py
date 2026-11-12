import json

with open("pokemones.json", "r") as archivo:
    pokemones = json.load(archivo)

for pokemon in pokemones:
    print("Pokemon:", pokemon["name"]["english"])
    print("Level:", pokemon["level"])
    print("Type:", pokemon["type"][0])


    print("----------------------")
        