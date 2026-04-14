my_list = []
for i in range(10):
    add = int(input("We are going to enter 10 numbers: "))
    my_list.append(add)
    smallest = my_list[0]

for i in range(len(my_list)):
    if (smallest > my_list[i]):
        smallest = my_list[i]

print(my_list)
print(f"The smallest number is: {smallest}")