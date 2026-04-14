"""first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util'] 
third_list = ['1', '2', '3', '4', '5', '6']
for i in range(len(first_list)):
        print(first_list[i], second_list[i], third_list[i])"""

"""my_string = "Pizza con piña"
for i in range(len(my_string)-1, -1, -1):
    print(my_string[i])"""

"""lista = [1, 2, 3, 4, 5]

temp = lista[0]              
lista[0] = lista[len(lista)-1]   
lista[len(lista)-1] = temp       

print(lista)"""""

"""my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(my_list)-1, -1, -1):
    resultado = my_list[i] % 2
    if (resultado != 0 ):
        my_list.pop(i)

print(my_list)"""

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

