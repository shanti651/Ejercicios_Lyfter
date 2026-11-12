def ask_for_sentence_and_add(path):
    sentence = input("Write a sentence to append: ")
    with open(path, "a") as file:
        file.write(sentence + "\n")

ask_for_sentence_and_add("Ejercicio 4 manejo de archivos extras.txt")

with open("Ejercicio 4 manejo de archivos extras.txt", "r") as file:
    sentence = file.read()
print(f"you have written: {sentence}")