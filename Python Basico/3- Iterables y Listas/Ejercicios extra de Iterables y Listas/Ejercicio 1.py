my_list = []
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
print(f"The number {search} appears {counter} times")