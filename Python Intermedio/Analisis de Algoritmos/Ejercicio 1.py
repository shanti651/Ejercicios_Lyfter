def bubble_sort(arr):
    n = len(arr) # O(1)
    for i in range(n): # O(n)
        for j in range(n - i - 1): # O(n^2)
            if arr[j] > arr[j + 1]: # O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # O(1)

my_list = [10, 3, 6, 7, 2, 1, 9] # O(1)
bubble_sort(my_list) # O(n)
print(my_list)

#Bubble sort es una funcion O(n) porque tiene ciclos anidados 