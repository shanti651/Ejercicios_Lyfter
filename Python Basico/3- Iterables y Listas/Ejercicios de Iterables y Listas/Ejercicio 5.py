my_list = []
for i in range(10):
    agregate = int(input("Type 10 numbers: "))
    my_list.append(agregate)
    mayor = my_list[0]

for i in range(len(my_list)):
    if (mayor < my_list[i]):
        mayor = my_list[i]

print(my_list)
print (f"The highest number is: {mayor}")