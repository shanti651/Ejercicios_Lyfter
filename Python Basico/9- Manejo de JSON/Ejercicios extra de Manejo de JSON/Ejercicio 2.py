import json

with open("pokemones.json", "r") as archivo:
    pokemones = json.load(archivo)

poke = input("What is the type of the Pokemon? ")
for pokemon in pokemones: 
    if poke == pokemon["type"][0]:
        print("Pokemon:", pokemon["name"]["english"])

for pokemon in pokemones:
    print("Pokemon:", pokemon["name"]["english"])
    print("Stats:")
    for stat, valor in pokemon["base"].items():
        print(f"  {stat}: {valor}")
        