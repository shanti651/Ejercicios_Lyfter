import json

with open("pokemones.json", "r") as archivo:
    pokemones = json.load(archivo)

for pokemon in pokemones:
    print("Pokemon:", pokemon["name"]["english"])
    print("Level:", pokemon["level"])
    print("Type:", pokemon["type"][0])


    print("----------------------")

poke = input("What is the type of the Pokemon? ")
for pokemon in pokemones: 
    if poke == pokemon["type"][0]:
        print("Pokemon:", pokemon["name"]["english"])

for pokemon in pokemones:
    print("Pokemon:", pokemon["name"]["english"])
    print("Stats:")
    for stat, valor in pokemon["base"].items():
        print(f"  {stat}: {valor}")




types = {}

for pokemon in pokemones:
    type = pokemon["type"][0]
    level = pokemon["level"]

    if type not in types:
        types[type] = []

    types[type].append(level)

for type, level in types.items():
    promedio = sum(level) / len(level)
    print(f"Tipo: {type} → Promedio de nivel: {promedio: }")
