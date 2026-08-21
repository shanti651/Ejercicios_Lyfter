def validar_numeros(funcion_original):
    def funcion_copia(a, b):
        try:
            a + 0
        except TypeError:
            raise TypeError(f"El parámetro {a!r} no es un número")

        try:
            b + 0
        except TypeError:
            raise TypeError(f"El parámetro {b!r} no es un número")

        return funcion_original(a, b)
    return funcion_copia


@validar_numeros
def sumar(a, b):
    return a + b


print(sumar(3, 4))        
print(sumar(3, "hola"))  