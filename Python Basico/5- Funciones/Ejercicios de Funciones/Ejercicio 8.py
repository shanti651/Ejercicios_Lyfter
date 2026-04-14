numbers = [1, 2, 4, 6, 7, 13, 9, 67]

def function(numbers):
    numbers2 = []

    for x in numbers:
        if x <= 1:
            continue

        is_prime = True

        for i in range(2, x):
            if x % i == 0:
                is_prime = False
                break

        if is_prime:
            numbers2.append(x)

    return numbers2


result = function(numbers)
print(result)