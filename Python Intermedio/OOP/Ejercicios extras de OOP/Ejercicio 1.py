class Rectangle:

    def __init__(self, width, height):

        if width < 0 or height < 0:
            raise ValueError(
                "Existe un valor negativo, los valores deben ser positivos"
            )

        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
try:
    height = int(input("Ingrese la altura: "))
    width = int(input("Ingrese el ancho: "))

    rectangle = Rectangle(width, height)

    print(rectangle.get_area())
    print(rectangle.get_perimeter())

except ValueError as e:
    print(e)