my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(my_list)-1, -1, -1):
    resultado = my_list[i] % 2
    if (resultado != 0 ):
        my_list.pop(i)

print(my_list)