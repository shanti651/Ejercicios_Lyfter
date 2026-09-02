class Circle:

    def __init__(self):
        self.radio = float(input("what is the radio?"))

        
    def get_area(self):
        area = 3.14 * (self.radio **2)
        return area
    
c1 = Circle()
print(c1.get_area())

