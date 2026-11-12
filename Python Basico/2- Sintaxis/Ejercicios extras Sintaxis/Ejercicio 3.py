number = int(input("Enter a number"))
counter = 1
sum_result = 0
result = 0
while (counter <= number):
    sum_result = sum_result + counter
    counter = counter + 1

print(f"The result of the sum is {sum_result}")