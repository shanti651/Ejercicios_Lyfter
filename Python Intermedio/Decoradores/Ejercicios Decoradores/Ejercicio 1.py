def decorador(funcion_original):
    def funcion_copia(*args, **kwargs):
        print(f"Parámetros recibidos: args={args}, kwargs={kwargs}")
        resultado = funcion_original(*args, **kwargs)
        print(f"La función retornó: {resultado}")
        return resultado
    return funcion_copia


@decorador
def saludar(nombre):
    print(f"Hola, {nombre}")
    return f"saludo a {nombre} completado"


resultado_final = saludar("Ana")
print(resultado_final)