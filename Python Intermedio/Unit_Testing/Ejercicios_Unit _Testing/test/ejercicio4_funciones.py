def string(text):
    result = ""
    for x in text:
        result = x + result
    return result

print(string("hello world"))