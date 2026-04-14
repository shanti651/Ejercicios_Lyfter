def filter_words(word_list, number):
    new_list = []
    for x in word_list:
        if len(x) > number:
            new_list.append(x)
    return new_list

def ask_data():
    words = []
    for x in range(5):
        word = input("Type 5 words: ")
        words.append(word)
    letters = int(input("How many letters minimum should the words have: "))
    return words, letters

words, letters = ask_data()
result = filter_words(words, letters)
print(result)
