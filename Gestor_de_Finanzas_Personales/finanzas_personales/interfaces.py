import FreeSimpleGUI as sg

from logica import NOMBRES_MESES, quitar_decimales

sg.theme("LightGrey1")


def se_cerro(evento):
    if evento == sg.WIN_CLOSED or evento == "-CANCELAR-" or evento == "-SALIR-":
        return True
    return False




def crear_fila_dato(texto, key_valor, key_texto=None):
    return [sg.Text(texto, key=key_texto, size=(26, 1)),
            sg.Text("₡0.00", key=key_valor, size=(16, 1), justification="right")]


def crear_ventana_principal():
    anios = []
    for anio in range(2020, 2031):
        anios.append(anio)

    fila_mes = [
        sg.Button("◀", key="-MES_ANTERIOR-"),
        sg.Text("Mes:"),
        sg.Combo(NOMBRES_MESES, key="-MES-", readonly=True, enable_events=True, size=(12, 1)),
        sg.Text("Año:"),
        sg.Combo(anios, key="-ANIO-", readonly=True, enable_events=True, size=(6, 1)),
        sg.Button("▶", key="-MES_SIGUIENTE-"),
    ]

    fila_filtro = [
        sg.Text("Fecha inicio:"),
        sg.Input(key="-INICIO-", size=(12, 1)),
        sg.CalendarButton("Elegir", target="-INICIO-", format="%d/%m/%Y"),
        sg.Text("Fecha fin:"),
        sg.Input(key="-FIN-", size=(12, 1)),
        sg.CalendarButton("Elegir", target="-FIN-", format="%d/%m/%Y"),
        sg.Button("Filtrar", key="-FILTRAR-"),
        sg.Button("Mostrar todo", key="-MOSTRAR_TODO-"),
    ]

    tabla = sg.Table(
        values=[],
        headings=["Fecha", "Título", "Monto", "Categoría", "Tipo"],
        key="-TABLA-",
        auto_size_columns=False,
        col_widths=[11, 25, 15, 15, 9],
        justification="left",
        num_rows=15,
    )


    panel_salario = sg.Frame("Salario", [
        [sg.Text("", key="-TITULO_SALARIO-", font=("Helvetica", 12, "bold"))],
        [sg.Text("", key="-MODALIDAD-")],
        [sg.pin(sg.Button("Ingresar salario mensual", key="-PAGO_MENSUAL-")),
         sg.pin(sg.Button("IQ", key="-PAGO_IQ-", size=(6, 1))),
         sg.pin(sg.Button("IIQ", key="-PAGO_IIQ-", size=(6, 1)))],
        [sg.Text("", key="-PAGOS-", size=(42, 1))],
        crear_fila_dato("Salario bruto:", "-BRUTO-"),
        crear_fila_dato("CCSS (10.83%):", "-CCSS-"),
        crear_fila_dato("Impuesto sobre la renta:", "-RENTA-"),
        crear_fila_dato("Asociación solidarista:", "-ASOCIACION-", "-TEXTO_ASOCIACION-"),
        crear_fila_dato("Total de rebajos:", "-TOTAL_REBAJOS-"),
        crear_fila_dato("Salario neto:", "-NETO-"),
        [sg.Text("", key="-PENDIENTES-", text_color="red", size=(42, 1))],
        [sg.Button("Configurar salario", key="-CONFIGURAR-")],
    ], vertical_alignment="top")

    fila_botones = [
        sg.Button("Agregar categoría", key="-AGREGAR_CATEGORIA-"),
        sg.Button("Agregar gasto", key="-AGREGAR_GASTO-"),
        sg.Button("Agregar ingreso", key="-AGREGAR_INGRESO-"),
        sg.Button("Exportar a CSV", key="-EXPORTAR-"),
        sg.Button("Aguinaldo", key="-AGUINALDO-"),
        sg.Button("Salir", key="-SALIR-"),
    ]

    layout = [
        [sg.Text("Finanzas personales", font=("Helvetica", 16, "bold"))],
        fila_mes,
        fila_filtro,
        [sg.Text("", key="-TITULO_TABLA-", font=("Helvetica", 11, "bold"))],
        [tabla, panel_salario],
        [sg.Text("", key="-TOTALES-", font=("Helvetica", 11, "bold"))],
        fila_botones,
    ]

    return sg.Window("Finanzas personales", layout, finalize=True)




def crear_ventana_categoria():
    layout = [
        [sg.Text("Nombre:", size=(10, 1)), sg.Input(key="-NOMBRE-", size=(25, 1))],
        [sg.Text("Color:", size=(10, 1)),
         sg.Input("#FFFFFF", key="-COLOR-", size=(10, 1)),
         sg.ColorChooserButton("Elegir color", target="-COLOR-")],
        [sg.Button("Guardar", key="-GUARDAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
    ]
    return sg.Window("Nueva categoría", layout, modal=True)


def crear_ventana_movimiento(tipo, categorias, fecha_texto):
    layout = [
        [sg.Text("Título:", size=(10, 1)), sg.Input(key="-TITULO-", size=(25, 1))],
        [sg.Text("Monto (₡):", size=(10, 1)), sg.Input(key="-MONTO-", size=(25, 1))],
        [sg.Text("Categoría:", size=(10, 1)),
         sg.Combo(categorias, default_value=categorias[0], key="-CATEGORIA-", readonly=True, size=(23, 1))],
        [sg.Text("Fecha:", size=(10, 1)),
         sg.Input(fecha_texto, key="-FECHA-", size=(12, 1)),
         sg.CalendarButton("Elegir", target="-FECHA-", format="%d/%m/%Y")],
        [sg.Button("Guardar", key="-GUARDAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
    ]
    return sg.Window("Nuevo " + tipo.lower(), layout, modal=True)


def crear_ventana_configuracion(es_quincenal, tiene_asociacion, porcentaje, nombre_mes):
    if tiene_asociacion:
        texto_porcentaje = str(quitar_decimales(porcentaje))
    else:
        texto_porcentaje = ""

    layout = [
        [sg.Text("¿Cómo desea ingresar su salario?", font=("Helvetica", 11, "bold"))],
        [sg.Radio("Mensual", "MODALIDAD", key="-RADIO_MENSUAL-", default=not es_quincenal),
         sg.Radio("Quincenal (IQ y IIQ)", "MODALIDAD", key="-RADIO_QUINCENAL-", default=es_quincenal)],
        [sg.Text("Se aplica a " + nombre_mes + " y a los meses nuevos.")],
        [sg.Text("¿Está en una asociación solidarista?", font=("Helvetica", 11, "bold"))],
        [sg.Radio("Sí", "ASOCIACION", key="-SI-", default=tiene_asociacion, enable_events=True),
         sg.Radio("No", "ASOCIACION", key="-NO-", default=not tiene_asociacion, enable_events=True)],
        [sg.Text("Porcentaje que le rebaja (%):"),
         sg.Input(texto_porcentaje, key="-PORCENTAJE-", size=(8, 1), disabled=not tiene_asociacion)],
        [sg.Button("Continuar", key="-GUARDAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
    ]
    return sg.Window("Configuración del salario", layout, modal=True)


def crear_ventana_aguinaldo(anio):
    anios = []
    for numero in range(2020, 2031):
        anios.append(numero)

    layout = [
        [sg.Text("Aguinaldo de diciembre:", font=("Helvetica", 12, "bold")),
         sg.Combo(anios, default_value=anio, key="-ANIO_AGUINALDO-", readonly=True,
                  enable_events=True, size=(6, 1))],
        [sg.Text("", key="-PERIODO-")],
        [sg.Table(values=[], headings=["Mes", "Salario bruto", "Estado"], key="-TABLA_AGUINALDO-",
                  auto_size_columns=False, col_widths=[16, 16, 14], justification="left", num_rows=12)],
        [sg.Text("", key="-TOTAL_BRUTO-")],
        [sg.Text("", key="-MESES_REGISTRADOS-")],
        [sg.Text("", key="-MONTO_AGUINALDO-", font=("Helvetica", 13, "bold"))],
        [sg.Text("El aguinaldo es la suma de los salarios brutos dividida entre 12.")],
        [sg.Text("No se le rebaja CCSS ni renta. Se paga a más tardar el 20 de diciembre.")],
        [sg.Button("Cerrar", key="-CANCELAR-")],
    ]
    return sg.Window("Aguinaldo", layout, modal=True, finalize=True)




def pedir_monto(mensaje, monto_actual):
    if monto_actual is None:
        texto_inicial = ""
    else:
        texto_inicial = str(quitar_decimales(monto_actual))
    return sg.popup_get_text(mensaje, title="Salario", default_text=texto_inicial)


def mostrar_error(mensaje):
    sg.popup_error(mensaje, title="Error")


def mostrar_mensaje(mensaje):
    sg.popup(mensaje, title="Información")


def pedir_ruta_csv():
    return sg.popup_get_file("¿Dónde desea guardar el archivo?", save_as=True,
                             default_path="movimientos.csv", file_types=(("CSV", "*.csv"),))
