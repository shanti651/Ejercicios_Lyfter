seconds = int(input("Enter the time in seconds "))
objective = 0
if (seconds < 600):
    objective = 600 - seconds
    print(f"{objective} seconds are missing to reach 10 minutes")
elif (seconds > 600):
    print("Greater")
elif (seconds == 600):
    print("Equal")