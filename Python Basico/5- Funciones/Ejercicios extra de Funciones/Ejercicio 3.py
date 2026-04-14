def function(string):
    total = 0
    for x in string:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            total = total + 1
    return total

sentence = input("Type a Word or Phrase: ")
result = function(sentence)
print(result)