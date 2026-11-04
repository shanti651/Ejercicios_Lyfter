#1-
"""def second_function():
    print("Hello, I am the second function.")

    
def first_function():
    print("Hello, I am the first function.")
    second_function()  

    
first_function()"""

#2
"""def function():
    x = 10 
    print("Inside the function, x =", x)


function()
print("Outside the function, x =", x)"""

"""global_variable = 5  

def change_global_variable():
    print("Inside the function, global variable =", global_variable)
    return global_variable + 1


print("Before the function, global variable is =", global_variable)
global_variable = change_global_variable()
print("After the function, global variable is =", global_variable)"""

#3
my_list = [4, 6, 2, 29]

"""def sum_my_list(my_list):
    total = 0
    for i in my_list:
        total = i + total
    return total


print(sum_my_list(my_list))"""

#4
"""def string(text):
    result = ""
    for x in text:
        result = x + result
    return result

print(string("hello world"))"""
    
string = "I like FC Barcelona"

#5
"""def function(string):
    uppercase = 0
    lowercase = 0
    for x in string:
        if x.isupper():
            uppercase = uppercase + 1
        elif x.islower():
            lowercase = lowercase + 1
    print(f"the sentence has {uppercase} uppercase letters and {lowercase} lowercase letters")

function(string)"""

#6
"""def sort_string(text):
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

print(sort_string("python-variable-function-computer-monitor"))"""

#7
numbers = [1, 4, 6, 7, 13, 9, 67]

def function(numbers):
    numbers2 = []
    for x in numbers:
        if x <= 1:
            print("1 is not prime")
        else:
            is_prime = True  
            
            for i in range(2, x):
                if x % i == 0:
                    print(f"{x} is not a prime number")
                    is_prime = False
                    break   
            
            if is_prime:
                numbers2.append(x)
    
    return numbers2

result = function(numbers)
print(result)


"""numbers = [1, 2, 4, 6, 7, 13, 9, 67]

def function(numbers):
    numbers2 = []

    for x in numbers:
        if x <= 1:
            continue

        is_prime = True

        for i in range(2, x):
            if x % i == 0:
                is_prime = False
                break

        if is_prime:
            numbers2.append(x)

    return numbers2


result = function(numbers)
print(result)"""

