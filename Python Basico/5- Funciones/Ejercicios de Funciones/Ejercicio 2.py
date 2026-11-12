def function():
    x = 10 
    print("Inside the function, x =", x)


function()
print("Outside the function, x =", x)

global_variable = 5  

def change_global_variable():
    print("Inside the function, global variable =", global_variable)
    return global_variable + 1


print("Before the function, global variable is =", global_variable)
global_variable = change_global_variable()
print("After the function, global variable is =", global_variable)