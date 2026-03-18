"""my_list = []
print("We are going to enter 10 numbers:")
for i in range(10):
    add = int(input(f"Enter number {i + 1}: "))
    my_list.append(add)

search = int(input("Enter the number you want to search for: "))
counter = 0

for number in my_list:
    if (search == number):
        counter = counter + 1

print(my_list)
print(f"The number {search} appears {counter} times")"""

"""my_list = [1, -2, 3, 4, 5, -6, 0]
for number in my_list:
    if (number <= 0):
        print("There is at least one negative number or zero")"""

"""my_list = []
for i in range(10):
    add = int(input("We are going to enter 10 numbers: "))
    my_list.append(add)
    smallest = my_list[0]

for i in range(len(my_list)):
    if (smallest > my_list[i]):
        smallest = my_list[i]

print(my_list)
print(f"The smallest number is: {smallest}")"""

"""my_list = []
updated_list = []
for i in range(10):
    add = int(input("We are going to enter 10 numbers: "))
    my_list.append(add)
suma = 0
for number in my_list:
    suma = suma + number

average = suma / 10

for i in my_list:
    if (i > average):
        updated_list.append(i)

print(my_list)
print(average)
print(updated_list)"""

my_list = []
updated_list = []
for i in range(5):
    add = input("Enter 5 words: ")
    my_list.append(add)
    
for word in my_list:
    if len(word) > 4:
        updated_list.append(word)

print(my_list)
print(updated_list)









