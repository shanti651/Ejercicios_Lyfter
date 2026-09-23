def bubble_sort(list):
    n = len(list) # O(1)
    for i in range(n): # O(1)
        for j in range(n - i - 1): # O(n^2)
            if list[j] > list[j + 1]: # O(1)
                list[j], list[j + 1] = list[j + 1], list[j] # O(1)

my_list = [10, 3, 6, 7, 2, 1, 9] # O(1)
bubble_sort(my_list) # O(1)
print(my_list)