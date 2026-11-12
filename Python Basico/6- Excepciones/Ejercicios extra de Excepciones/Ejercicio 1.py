def function():
    word = input("Type a word: ")
    letter = input("Which letter do you want to search:")
    total = 0
    for x in word:
        if x == letter:
            total = total + 1
    return total

result = function()
print(f"The letter is {result} times in that word")