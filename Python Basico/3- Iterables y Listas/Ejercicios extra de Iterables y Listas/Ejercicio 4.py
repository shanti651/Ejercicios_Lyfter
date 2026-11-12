my_list = []
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
print(updated_list)