def function(string):
    uppercase = 0
    lowercase = 0
    for x in string:
        if x.isupper():
            uppercase = uppercase + 1
        elif x.islower():
            lowercase = lowercase + 1
    return uppercase, lowercase




