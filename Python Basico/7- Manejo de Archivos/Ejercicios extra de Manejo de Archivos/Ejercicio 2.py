def open_and_count_words(path):
    with open(path, "r") as file:
        contenido = file.read()
    word = contenido.split()
    count = len(word)
    return count

number_of_words = open_and_count_words("ejercicio 1 de manejo de archivos extra corregido.txt")

print(f"This file has {number_of_words} words")