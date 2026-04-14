string = "I like FC Barcelona"

def function(string):
    uppercase = 0
    lowercase = 0
    for x in string:
        if x.isupper():
            uppercase = uppercase + 1
        elif x.islower():
            lowercase = lowercase + 1
    print(f"the sentence has {uppercase} uppercase letters and {lowercase} lowercase letters")

function(string)