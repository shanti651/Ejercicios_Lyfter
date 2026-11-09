from datetime import date

import interfaces
import persistencia
from aguinaldo import calcular_aguinaldo
from logica import (NOMBRES_MESES, GestorFinanzas, formatear_colones, obtener_nombre_mes,
                    quitar_decimales)
from salario import ConfiguracionSalario




def cargar_gestor():
    gestor = GestorFinanzas()
    try:
        datos = persistencia.cargar_json(persistencia.ARCHIVO_FINANZAS)
        if datos is not None:
            gestor.cargar_desde_diccionario(datos)
    except (ValueError, KeyError):
        interfaces.mostrar_error("No se pudieron cargar los movimientos. Se empieza sin datos.")
        gestor = GestorFinanzas()
    return gestor


def guardar_gestor(gestor):
    persistencia.guardar_json(gestor.convertir_a_diccionario(), persistencia.ARCHIVO_FINANZAS)


def cargar_salario():
    configuracion = ConfiguracionSalario()
    try:
        datos = persistencia.cargar_json(persistencia.ARCHIVO_SALARIO)
        if datos is not None:
            configuracion.cargar_desde_diccionario(datos)
    except (ValueError, KeyError):
        interfaces.mostrar_error("No se pudo cargar el salario. Se empieza sin datos.")
        configuracion = ConfiguracionSalario()
    return configuracion


def guardar_salario(configuracion):
    persistencia.guardar_json(configuracion.convertir_a_diccionario(), persistencia.ARCHIVO_SALARIO)




def mostrar_movimientos(ventana, gestor, movimientos, titulo):
    filas = []
    colores = []
    numero_fila = 0
    for movimiento in movimientos:
        filas.append(movimiento.convertir_a_fila())
        color = gestor.obtener_color(movimiento.categoria)
        colores.append((numero_fila, "black", color))
        numero_fila = numero_fila + 1

    ventana["-TABLA-"].update(values=filas, row_colors=colores)
    ventana["-TITULO_TABLA-"].update(titulo)

    ingresos = gestor.calcular_total_ingresos(movimientos)
    gastos = gestor.calcular_total_gastos(movimientos)
    balance = gestor.calcular_balance(movimientos)
    ventana["-TOTALES-"].update("Ingresos: " + formatear_colones(ingresos) +
                                "    Gastos: " + formatear_colones(gastos) +
                                "    Balance: " + formatear_colones(balance))


def mostrar_todo(ventana, gestor):
    ventana["-INICIO-"].update("")
    ventana["-FIN-"].update("")
    mostrar_movimientos(ventana, gestor, gestor.obtener_movimientos_ordenados(), "Todos los movimientos")


def mostrar_rebajo(monto):
    if monto == 0:
        return formatear_colones(0)
    return "- " + formatear_colones(monto)


def mostrar_salario(ventana, configuracion, anio, mes):
    modalidad = configuracion.obtener_modalidad_del_mes(anio, mes)
    salario_mes = configuracion.obtener_mes(anio, mes)
    desglose = configuracion.calcular_desglose(anio, mes)

  
    if modalidad == "Quincenal":
        ventana["-PAGO_MENSUAL-"].update(visible=False)
        ventana["-PAGO_IQ-"].update(visible=True)
        ventana["-PAGO_IIQ-"].update(visible=True)
        nombres_pagos = ["IQ", "IIQ"]
    else:
        ventana["-PAGO_MENSUAL-"].update(visible=True)
        ventana["-PAGO_IQ-"].update(visible=False)
        ventana["-PAGO_IIQ-"].update(visible=False)
        nombres_pagos = ["Mensual"]

 
    texto_pagos = ""
    pendientes = []
    for nombre_pago in nombres_pagos:
        monto = None
        if salario_mes is not None:
            monto = salario_mes.obtener_monto(nombre_pago)
        if monto is None:
            texto_pagos = texto_pagos + nombre_pago + ": pendiente   "
            pendientes.append(nombre_pago)
        else:
            texto_pagos = texto_pagos + nombre_pago + ": " + formatear_colones(monto) + "   "

    if configuracion.tiene_asociacion():
        porcentaje = quitar_decimales(configuracion.porcentaje_asociacion)
        texto_asociacion = "Asociación solidarista (" + str(porcentaje) + "%):"
    else:
        texto_asociacion = "Asociación solidarista (no aplica):"

    if len(pendientes) > 0:
        texto_pendientes = "Falta ingresar: " + ", ".join(pendientes)
    else:
        texto_pendientes = ""

    ventana["-TITULO_SALARIO-"].update("Salario de " + obtener_nombre_mes(anio, mes))
    ventana["-MODALIDAD-"].update("Modalidad: " + modalidad)
    ventana["-PAGOS-"].update(texto_pagos)
    ventana["-BRUTO-"].update(formatear_colones(desglose["bruto"]))
    ventana["-CCSS-"].update(mostrar_rebajo(desglose["ccss"]))
    ventana["-RENTA-"].update(mostrar_rebajo(desglose["renta"]))
    ventana["-TEXTO_ASOCIACION-"].update(texto_asociacion)
    ventana["-ASOCIACION-"].update(mostrar_rebajo(desglose["asociacion"]))
    ventana["-TOTAL_REBAJOS-"].update(mostrar_rebajo(desglose["total_rebajos"]))
    ventana["-NETO-"].update(formatear_colones(desglose["neto"]))
    ventana["-PENDIENTES-"].update(texto_pendientes)


def mostrar_mes(ventana, gestor, configuracion, anio, mes):
    ventana["-MES-"].update(value=NOMBRES_MESES[mes - 1])
    ventana["-ANIO-"].update(value=anio)
    ventana["-INICIO-"].update("")
    ventana["-FIN-"].update("")
    titulo = "Movimientos de " + obtener_nombre_mes(anio, mes)
    mostrar_movimientos(ventana, gestor, gestor.filtrar_por_mes(anio, mes), titulo)
    mostrar_salario(ventana, configuracion, anio, mes)


def accion_filtrar(ventana, gestor, valores):
    try:
        movimientos = gestor.filtrar_por_fechas(valores["-INICIO-"], valores["-FIN-"])
    except ValueError as error:
        interfaces.mostrar_error(str(error))
        return
    titulo = "Movimientos del " + valores["-INICIO-"] + " al " + valores["-FIN-"]
    mostrar_movimientos(ventana, gestor, movimientos, titulo)




def accion_agregar_categoria(gestor):
    ventana = interfaces.crear_ventana_categoria()
    while True:
        evento, valores = ventana.read()
        if interfaces.se_cerro(evento):
            break
        if evento == "-GUARDAR-":
            try:
                gestor.agregar_categoria(valores["-NOMBRE-"], valores["-COLOR-"])
            except ValueError as error:
                interfaces.mostrar_error(str(error))
                continue  
            guardar_gestor(gestor)
            break
    ventana.close()


def accion_agregar_movimiento(gestor, tipo, anio, mes):
    if len(gestor.categorias) == 0:
        interfaces.mostrar_error("No hay categorías disponibles. Agregue una categoría primero.")
        return None


    hoy = date.today()
    if anio == hoy.year and mes == hoy.month:
        fecha = hoy
    else:
        fecha = date(anio, mes, 1)

    ventana = interfaces.crear_ventana_movimiento(tipo, gestor.obtener_nombres_categorias(),
                                                  fecha.strftime("%d/%m/%Y"))
    movimiento = None
    while True:
        evento, valores = ventana.read()
        if interfaces.se_cerro(evento):
            break
        if evento == "-GUARDAR-":
            try:
                movimiento = gestor.agregar_movimiento(valores["-TITULO-"], valores["-MONTO-"],
                                                       valores["-CATEGORIA-"], tipo, valores["-FECHA-"])
            except ValueError as error:
                interfaces.mostrar_error(str(error))
                continue
            guardar_gestor(gestor)
            break
    ventana.close()

    if movimiento is not None:
        interfaces.mostrar_mensaje("Nuevo " + tipo.lower() + " agregado:\n" + str(movimiento))
    return movimiento


def accion_exportar_csv(gestor):
    if len(gestor.movimientos) == 0:
        interfaces.mostrar_error("No hay movimientos para exportar.")
        return

    ruta = interfaces.pedir_ruta_csv()
    if ruta is None or ruta == "":
        return

    movimientos = gestor.obtener_movimientos_ordenados()
    filas = []
    for movimiento in movimientos:
        filas.append(movimiento.convertir_a_fila_csv())

    totales = [
        "Totales:",
        "Ingresos: ₡" + str(quitar_decimales(gestor.calcular_total_ingresos(movimientos))),
        "Gastos: ₡" + str(quitar_decimales(gestor.calcular_total_gastos(movimientos))),
        "Balance Neto: ₡" + str(quitar_decimales(gestor.calcular_balance(movimientos))),
    ]
    persistencia.exportar_csv(ruta, filas, totales)
    interfaces.mostrar_mensaje("Archivo exportado en:\n" + ruta)




def accion_configurar_salario(configuracion, anio, mes):
    es_quincenal = configuracion.obtener_modalidad_del_mes(anio, mes) == "Quincenal"
    ventana = interfaces.crear_ventana_configuracion(es_quincenal, configuracion.tiene_asociacion(),
                                                     configuracion.porcentaje_asociacion,
                                                     obtener_nombre_mes(anio, mes))
    se_guardo = False
    while True:
        evento, valores = ventana.read()
        if interfaces.se_cerro(evento):
            break


        if evento == "-SI-" or evento == "-NO-":
            ventana["-PORCENTAJE-"].update(disabled=not valores["-SI-"])

        if evento == "-GUARDAR-":
            if valores["-RADIO_QUINCENAL-"]:
                modalidad = "Quincenal"
            else:
                modalidad = "Mensual"
            try:
                configuracion.configurar(modalidad, valores["-SI-"], valores["-PORCENTAJE-"], anio, mes)
            except ValueError as error:
                interfaces.mostrar_error(str(error))
                continue
            guardar_salario(configuracion)
            se_guardo = True
            break

    ventana.close()
    return se_guardo


def accion_ingresar_pago(configuracion, anio, mes, nombre_pago):
    salario_mes = configuracion.obtener_mes(anio, mes)
    monto_actual = None
    if salario_mes is not None:
        monto_actual = salario_mes.obtener_monto(nombre_pago)

    if nombre_pago == "Mensual":
        nombre = "salario mensual"
    else:
        nombre = nombre_pago

    mensaje = ("Monto bruto de " + nombre + " de " + obtener_nombre_mes(anio, mes) + " (₡)\n"
               "Incluya horas extra y comisiones, porque cuentan para el aguinaldo.")

    while True:
        texto = interfaces.pedir_monto(mensaje, monto_actual)
        if texto is None: 
            return False
        try:
            configuracion.registrar_pago(anio, mes, nombre_pago, texto)
        except ValueError as error:
            interfaces.mostrar_error(str(error))
            continue
        guardar_salario(configuracion)
        return True


def mostrar_aguinaldo(ventana, configuracion, anio):
    resultado = calcular_aguinaldo(configuracion, anio)

    if resultado["meses_registrados"] == 12:
        texto_monto = "Aguinaldo total: " + formatear_colones(resultado["aguinaldo"])
    else:
        texto_monto = "Aguinaldo acumulado: " + formatear_colones(resultado["aguinaldo"])

    ventana["-PERIODO-"].update("Periodo: del 01/12/" + str(anio - 1) + " al 30/11/" + str(anio))
    ventana["-TABLA_AGUINALDO-"].update(values=resultado["filas"])
    ventana["-TOTAL_BRUTO-"].update("Suma de salarios brutos: " + formatear_colones(resultado["total_bruto"]))
    ventana["-MESES_REGISTRADOS-"].update("Meses registrados: " + str(resultado["meses_registrados"]) + " de 12")
    ventana["-MONTO_AGUINALDO-"].update(texto_monto)


def accion_ver_aguinaldo(configuracion):
    anio = date.today().year
    ventana = interfaces.crear_ventana_aguinaldo(anio)
    mostrar_aguinaldo(ventana, configuracion, anio)

    while True:
        evento, valores = ventana.read()
        if interfaces.se_cerro(evento):
            break
        if evento == "-ANIO_AGUINALDO-":
            mostrar_aguinaldo(ventana, configuracion, int(valores["-ANIO_AGUINALDO-"]))

    ventana.close()
