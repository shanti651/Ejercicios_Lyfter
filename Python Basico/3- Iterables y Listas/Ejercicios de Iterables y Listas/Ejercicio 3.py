lista = [1, 2, 3, 4, 5]

temp = lista[0]              
lista[0] = lista[len(lista)-1]   
lista[len(lista)-1] = temp       

print(lista)