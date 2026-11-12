print("CALCULATOR")

def ask_number():
    while True:
        try:
            number1 = int(input("Type a number: "))
            break
        except ValueError:
            print("That was not a number")
    return number1

def ask_number_two():
    while True:
        try:
            number2 = int(input("Type the other number: "))
            break
        except ValueError:
            print("That was not a number")
    return number2

def menu():
    while True:
        do = input("What do you want to do? ADD = a SUBTRACT = b MULTIPLY = c DIVIDE = d CLEAR = e EXIT = z: ")
        return do

def function_add(number1, number2):
    number1 = number1 + number2
    return number1

def function_substract(number1, number2):
    number1 = number1 - number2
    return number1

def function_multiply(number1, number2):
    number1 = number1 * number2
    return number1

def function_divide(number1, number2):
    number1 = number1 / number2
    return number1


def main():
    result = ask_number()

    while True:
        print(f"Current result: {result}")
        option = menu()

        if option == "z":
            break

        elif option == "e":
            result = 0
            continue

        elif option in ["a", "b", "c", "d"]:
            number2 = ask_number_two()

            if option == "a":
                result = function_add(result, number2)

            elif option == "b":
                result = function_substract(result, number2)

            elif option == "c":
                result = function_multiply(result, number2)

            elif option == "d":
                if number2 == 0:
                    print("You can't divide by zero")
                    continue
                result = function_divide(result, number2)

        else:
            print("Invalid option")

main()

