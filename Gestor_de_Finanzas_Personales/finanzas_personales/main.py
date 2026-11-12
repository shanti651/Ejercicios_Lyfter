from datetime import date

import acciones
import interfaces
from logica import NOMBRES_MESES


def main():
    gestor = acciones.cargar_gestor()
    configuracion = acciones.cargar_salario()

  
    hoy = date.today()
    anio = hoy.year
    mes = hoy.month


    acciones.accion_configurar_salario(configuracion, anio, mes)

    ventana = interfaces.crear_ventana_principal()
    acciones.mostrar_mes(ventana, gestor, configuracion, anio, mes)

    while True:
        evento, valores = ventana.read()

        if interfaces.se_cerro(evento):
            break


        if evento == "-MES-" or evento == "-ANIO-":
            mes = NOMBRES_MESES.index(valores["-MES-"]) + 1
            anio = int(valores["-ANIO-"])
            acciones.mostrar_mes(ventana, gestor, configuracion, anio, mes)

        elif evento == "-MES_ANTERIOR-":
            mes = mes - 1
            if mes == 0:
                mes = 12
                anio = anio - 1
            acciones.mostrar_mes(ventana, gestor, configuracion, anio, mes)

        elif evento == "-MES_SIGUIENTE-":
            mes = mes + 1
            if mes == 13:
                mes = 1
                anio = anio + 1
            acciones.mostrar_mes(ventana, gestor, configuracion, anio, mes)


        elif evento == "-AGREGAR_CATEGORIA-":
            acciones.accion_agregar_categoria(gestor)

        elif evento == "-AGREGAR_GASTO-" or evento == "-AGREGAR_INGRESO-":
            if evento == "-AGREGAR_GASTO-":
                tipo = "Gasto"
            else:
                tipo = "Ingreso"
            movimiento = acciones.accion_agregar_movimiento(gestor, tipo, anio, mes)
            if movimiento is not None:
                anio = movimiento.fecha.year
                mes = movimiento.fecha.month
                acciones.mostrar_mes(ventana, gestor, configuracion, anio, mes)

        elif evento == "-FILTRAR-":
            acciones.accion_filtrar(ventana, gestor, valores)

        elif evento == "-MOSTRAR_TODO-":
            acciones.mostrar_todo(ventana, gestor)

        elif evento == "-EXPORTAR-":
            acciones.accion_exportar_csv(gestor)

  
        elif evento == "-CONFIGURAR-":
            if acciones.accion_configurar_salario(configuracion, anio, mes):
                acciones.mostrar_salario(ventana, configuracion, anio, mes)

        elif evento == "-PAGO_MENSUAL-" or evento == "-PAGO_IQ-" or evento == "-PAGO_IIQ-":
            if evento == "-PAGO_MENSUAL-":
                nombre_pago = "Mensual"
            elif evento == "-PAGO_IQ-":
                nombre_pago = "IQ"
            else:
                nombre_pago = "IIQ"
            if acciones.accion_ingresar_pago(configuracion, anio, mes, nombre_pago):
                acciones.mostrar_salario(ventana, configuracion, anio, mes)

        elif evento == "-AGUINALDO-":
            acciones.accion_ver_aguinaldo(configuracion)


    acciones.guardar_gestor(gestor)
    acciones.guardar_salario(configuracion)
    ventana.close()


main()
