my_list = []
updated_list = []
for i in range(5):
    add = input("Enter 5 words: ")
    my_list.append(add)
    
for word in my_list:
    if len(word) > 4:
        updated_list.append(word)

print(my_list)
print(updated_list)
