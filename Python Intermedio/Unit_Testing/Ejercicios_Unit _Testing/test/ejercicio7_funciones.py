def function(numbers):
    numbers2 = []
    for x in numbers:
        if x <= 1:
            print("1 is not prime")
        else:
            is_prime = True  
            
            for i in range(2, x):
                if x % i == 0:
                    print(f"{x} is not a prime number")
                    is_prime = False
                    break   
            
            if is_prime:
                numbers2.append(x)
    
    return numbers2


