def validar_numeros(funcion_original):
    def funcion_copia(*args, **kwargs):
        for valor in args:
            if not isinstance(valor, (int, float)):
                raise TypeError(f"El parámetro {valor!r} no es un número")

        for clave, valor in kwargs.items():
            if not isinstance(valor, (int, float)):
                raise TypeError(f"El parámetro '{clave}={valor!r}' no es un número")

        return funcion_original(*args, **kwargs)
    return funcion_copia


@validar_numeros
def sumar(a, b):
    return a + b


print(sumar(3, 4))        
