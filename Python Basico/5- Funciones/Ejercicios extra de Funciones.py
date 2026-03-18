"""def function():
    word = input("Type a word: ")
    letter = input("Which letter do you want to search:")
    total = 0
    for x in word:
        if x == letter:
            total = total + 1
    return total

result = function()
print(f"The letter is {result} times in that word")"""




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



"""def function(string):
    total = 0
    for x in string:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            total = total + 1
    return total

sentence = input("Type a Word or Phrase: ")
result = function(sentence)
print(result)"""







