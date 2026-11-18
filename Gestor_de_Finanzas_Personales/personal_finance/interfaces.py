import FreeSimpleGUI as sg

from logic import FIRST_FORTNIGHT, MONTH_NAMES, MONTHLY, SECOND_FORTNIGHT, remove_decimals

sg.theme("LightGrey1")


def was_closed(event):
    if event == sg.WIN_CLOSED or event == "-CANCELAR-" or event == "-SALIR-":
        return True
    return False




def create_data_row(text, value_key, text_key=None):
    return [sg.Text(text, key=text_key, size=(26, 1)),
            sg.Text("₡0.00", key=value_key, size=(16, 1), justification="right")]


def create_main_window():
    years = []
    for year in range(2020, 2031):
        years.append(year)

    month_row = [
        sg.Button("◀", key="-MES_ANTERIOR-"),
        sg.Text("Mes:"),
        sg.Combo(MONTH_NAMES, key="-MES-", readonly=True, enable_events=True, size=(12, 1)),
        sg.Text("Año:"),
        sg.Combo(years, key="-ANIO-", readonly=True, enable_events=True, size=(6, 1)),
        sg.Button("▶", key="-MES_SIGUIENTE-"),
    ]

    filter_row = [
        sg.Text("Fecha inicio:"),
        sg.Input(key="-INICIO-", size=(12, 1)),
        sg.CalendarButton("Elegir", target="-INICIO-", format="%d/%m/%Y"),
        sg.Text("Fecha fin:"),
        sg.Input(key="-FIN-", size=(12, 1)),
        sg.CalendarButton("Elegir", target="-FIN-", format="%d/%m/%Y"),
        sg.Button("Filtrar", key="-FILTRAR-"),
        sg.Button("Mostrar todo", key="-MOSTRAR_TODO-"),
    ]

    table = sg.Table(
        values=[],
        headings=["Fecha", "Título", "Monto", "Categoría", "Tipo"],
        key="-TABLA-",
        auto_size_columns=False,
        col_widths=[11, 25, 15, 15, 9],
        justification="left",
        num_rows=15,
    )


    salary_panel = sg.Frame("Salario", [
        [sg.Text("", key="-TITULO_SALARIO-", font=("Helvetica", 12, "bold"))],
        [sg.Text("", key="-MODALIDAD-")],
        [sg.pin(sg.Button("Ingresar salario mensual", key="-PAGO_MENSUAL-")),
         sg.pin(sg.Button(FIRST_FORTNIGHT, key="-PAGO_IQ-", size=(6, 1))),
         sg.pin(sg.Button(SECOND_FORTNIGHT, key="-PAGO_IIQ-", size=(6, 1)))],
        [sg.Text("", key="-PAGOS-", size=(42, 1))],
        create_data_row("Salario bruto:", "-BRUTO-"),
        create_data_row("CCSS (10.83%):", "-CCSS-"),
        create_data_row("Impuesto sobre la renta:", "-RENTA-"),
        create_data_row("Asociación solidarista:", "-ASOCIACION-", "-TEXTO_ASOCIACION-"),
        create_data_row("Total de rebajos:", "-TOTAL_REBAJOS-"),
        create_data_row("Salario neto:", "-NETO-"),
        [sg.Text("", key="-PENDIENTES-", text_color="red", size=(42, 1))],
        [sg.Button("Configurar salario", key="-CONFIGURAR-")],
    ], vertical_alignment="top")

    button_row = [
        sg.Button("Agregar categoría", key="-AGREGAR_CATEGORIA-"),
        sg.Button("Agregar gasto", key="-AGREGAR_GASTO-"),
        sg.Button("Agregar ingreso", key="-AGREGAR_INGRESO-"),
        sg.Button("Exportar a CSV", key="-EXPORTAR-"),
        sg.Button("Aguinaldo", key="-AGUINALDO-"),
        sg.Button("Salir", key="-SALIR-"),
    ]

    layout = [
        [sg.Text("Finanzas personales", font=("Helvetica", 16, "bold"))],
        month_row,
        filter_row,
        [sg.Text("", key="-TITULO_TABLA-", font=("Helvetica", 11, "bold"))],
        [table, salary_panel],
        [sg.Text("", key="-TOTALES-", font=("Helvetica", 11, "bold"))],
        button_row,
    ]

    return sg.Window("Finanzas personales", layout, finalize=True)




def create_category_window():
    layout = [
        [sg.Text("Nombre:", size=(10, 1)), sg.Input(key="-NOMBRE-", size=(25, 1))],
        [sg.Text("Color:", size=(10, 1)),
         sg.Input("#FFFFFF", key="-COLOR-", size=(10, 1)),
         sg.ColorChooserButton("Elegir color", target="-COLOR-")],
        [sg.Button("Guardar", key="-GUARDAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
    ]
    return sg.Window("Nueva categoría", layout, modal=True)


def create_transaction_window(transaction_type, categories, date_text):
    layout = [
        [sg.Text("Título:", size=(10, 1)), sg.Input(key="-TITULO-", size=(25, 1))],
        [sg.Text("Monto (₡):", size=(10, 1)), sg.Input(key="-MONTO-", size=(25, 1))],
        [sg.Text("Categoría:", size=(10, 1)),
         sg.Combo(categories, default_value=categories[0], key="-CATEGORIA-", readonly=True, size=(23, 1))],
        [sg.Text("Fecha:", size=(10, 1)),
         sg.Input(date_text, key="-FECHA-", size=(12, 1)),
         sg.CalendarButton("Elegir", target="-FECHA-", format="%d/%m/%Y")],
        [sg.Button("Guardar", key="-GUARDAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
    ]
    return sg.Window("Nuevo " + transaction_type.lower(), layout, modal=True)


def create_config_window(is_biweekly, has_association, percentage, month_name):
    if has_association:
        percentage_label = str(remove_decimals(percentage))
    else:
        percentage_label = ""

    layout = [
        [sg.Text("¿Cómo desea ingresar su salario?", font=("Helvetica", 11, "bold"))],
        [sg.Radio(MONTHLY, "MODALIDAD", key="-RADIO_MENSUAL-", default=not is_biweekly),
         sg.Radio("Quincenal (IQ y IIQ)", "MODALIDAD", key="-RADIO_QUINCENAL-", default=is_biweekly)],
        [sg.Text("Se aplica a " + month_name + " y a los meses nuevos.")],
        [sg.Text("¿Está en una asociación solidarista?", font=("Helvetica", 11, "bold"))],
        [sg.Radio("Sí", "ASOCIACION", key="-SI-", default=has_association, enable_events=True),
         sg.Radio("No", "ASOCIACION", key="-NO-", default=not has_association, enable_events=True)],
        [sg.Text("Porcentaje que le rebaja (%):"),
         sg.Input(percentage_label, key="-PORCENTAJE-", size=(8, 1), disabled=not has_association)],
        [sg.Button("Continuar", key="-GUARDAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
    ]
    return sg.Window("Configuración del salario", layout, modal=True)


def create_christmas_bonus_window(year):
    years = []
    for number in range(2020, 2031):
        years.append(number)

    layout = [
        [sg.Text("Aguinaldo de diciembre:", font=("Helvetica", 12, "bold")),
         sg.Combo(years, default_value=year, key="-ANIO_AGUINALDO-", readonly=True,
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




def ask_amount(message, current_amount):
    if current_amount is None:
        initial_text = ""
    else:
        initial_text = str(remove_decimals(current_amount))
    return sg.popup_get_text(message, title="Salario", default_text=initial_text)


def show_error(message):
    sg.popup_error(message, title="Error")


def show_message(message):
    sg.popup(message, title="Información")


def ask_csv_path():
    return sg.popup_get_file("¿Dónde desea guardar el archivo?", save_as=True,
                             default_path="movimientos.csv", file_types=(("CSV", "*.csv"),))
