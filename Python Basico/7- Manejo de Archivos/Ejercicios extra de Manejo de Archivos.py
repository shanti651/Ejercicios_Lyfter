"""def open_and_create_other_file(path):
    with open(path, "r") as file:
                contenido = file.read()
    contenido = contenido.replace("\n", " ")
    with open("ejercicio 1 de manejo de archivos extra corregido.txt", "w") as file:
        file.write(contenido)
    return "ejercicio 1 de manejo de archivos extra corregido.txt"

open_and_create_other_file("ejercicio 1 de manejo de archivos extra.txt")

with open("ejercicio 1 de manejo de archivos extra corregido.txt", "r") as file:
    sentence = file.read()
print(sentence)"""


"""def open_and_count_words(path):
    with open(path, "r") as file:
        contenido = file.read()
    word = contenido.split()
    count = len(word)
    return count

number_of_words = open_and_count_words("ejercicio 1 de manejo de archivos extra corregido.txt")

print(f"This file has {number_of_words} words")"""

"""def switch_to_upper(path):
    with open(path, "r") as file:
        contenido = file.read()
    sentence = contenido.upper()
    with open("ejercicio 3 de manejo de archivos mayusuclas.txt", "w") as file:
        file.write(sentence)
    return "ejercicio 3 de manejo de archivos mayusuclas.txt"

switch_to_upper("ejercicio 1 de manejo de archivos extra corregido.txt")

with open("ejercicio 3 de manejo de archivos mayusuclas.txt", "r") as file:
    upper_sentence = file.read()
print(upper_sentence)"""

def ask_for_sentence_and_add(path):
    sentence = input("Write a sentence to append: ")
    with open(path, "a") as file:
        file.write(sentence + "\n")

ask_for_sentence_and_add("Ejercicio 4 manejo de archivos extras.txt")

with open("Ejercicio 4 manejo de archivos extras.txt", "r") as file:
    sentence = file.read()
print(f"you have written: {sentence}")











