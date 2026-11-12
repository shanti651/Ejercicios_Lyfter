def sort_string(text):
    words = []
    word = ""

    for letter in text:
        if letter == "-":
            words.append(word)
            word = ""
        else:
            word += letter
    words.append(word)  # last word

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] > words[j]:
                words[i], words[j] = words[j], words[i]

    result = ""
    for i in range(len(words)):
        result += words[i]
        if i != len(words) - 1:
            result += "-"

    return result

print(sort_string("python-variable-function-computer-monitor"))