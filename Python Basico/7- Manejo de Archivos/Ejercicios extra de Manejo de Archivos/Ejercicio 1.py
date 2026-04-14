def open_and_create_other_file(path):
    with open(path, "r") as file:
                contenido = file.read()
    contenido = contenido.replace("\n", " ")
    with open("ejercicio 1 de manejo de archivos extra corregido.txt", "w") as file:
        file.write(contenido)
    return "ejercicio 1 de manejo de archivos extra corregido.txt"

open_and_create_other_file("ejercicio 1 de manejo de archivos extra.txt")

with open("ejercicio 1 de manejo de archivos extra corregido.txt", "r") as file:
    sentence = file.read()
print(sentence)