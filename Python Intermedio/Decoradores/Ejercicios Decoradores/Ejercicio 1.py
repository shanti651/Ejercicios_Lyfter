def decorador(funcion_original):
    def funcion_decorada(nombre):
        print(f"Parámetro: {nombre}")
        resultado = funcion_original(nombre)
        print(f"La función retorno: {resultado}")
        return resultado
    return funcion_decorada


@decorador
def saludar(nombre):
    print(f"Hola, {nombre}")
    return f"saludo a {nombre} completado"


resultado_final = saludar("Ana")
print(resultado_final)