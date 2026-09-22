def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n-1, i, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]

my_list = [10, 3, 6, 7, 2, 1, 9]
bubble_sort(my_list)
print(my_list)
print(my_list)