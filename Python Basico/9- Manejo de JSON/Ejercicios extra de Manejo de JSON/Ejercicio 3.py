import json

with open("pokemones.json", "r") as archivo:
    pokemones = json.load(archivo)

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