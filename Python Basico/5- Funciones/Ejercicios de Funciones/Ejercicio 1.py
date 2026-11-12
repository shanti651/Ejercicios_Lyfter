def second_function():
    print("Hello, I am the second function.")

    
def first_function():
    print("Hello, I am the first function.")
    second_function()  

    
first_function()