def switch_to_upper(path):
    with open(path, "r") as file:
        contenido = file.read()
    sentence = contenido.upper()
    with open("ejercicio 3 de manejo de archivos mayusuclas.txt", "w") as file:
        file.write(sentence)
    return "ejercicio 3 de manejo de archivos mayusuclas.txt"

switch_to_upper("ejercicio 1 de manejo de archivos extra corregido.txt")

with open("ejercicio 3 de manejo de archivos mayusuclas.txt", "r") as file:
    upper_sentence = file.read()
print(upper_sentence)