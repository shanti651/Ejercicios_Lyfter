from datetime import date

import interfaces
import persistence
from christmas_bonus import calculate_christmas_bonus
from logic import (BIWEEKLY, FIRST_FORTNIGHT, MONTH_NAMES, MONTHLY, SECOND_FORTNIGHT, FinanceManager,
                   calculate_balance, calculate_total_expenses, calculate_total_income,
                   format_colones, get_month_name, remove_decimals)
from salary import SalaryConfig




def load_manager():
    manager = FinanceManager()
    try:
        data = persistence.load_json(persistence.FINANCE_FILE)
        if data is not None:
            manager.load_from_dict(data)
    except (ValueError, KeyError):
        interfaces.show_error("No se pudieron cargar los movimientos. Se empieza sin datos.")
        manager = FinanceManager()
    return manager


def save_manager(manager):
    persistence.save_json(manager.to_dict(), persistence.FINANCE_FILE)


def load_salary():
    config = SalaryConfig()
    try:
        data = persistence.load_json(persistence.SALARY_FILE)
        if data is not None:
            config.load_from_dict(data)
    except (ValueError, KeyError):
        interfaces.show_error("No se pudo cargar el salario. Se empieza sin datos.")
        config = SalaryConfig()
    return config


def save_salary(config):
    persistence.save_json(config.to_dict(), persistence.SALARY_FILE)




def show_transactions(window, manager, transactions, title):
    rows = []
    colors = []
    row_number = 0
    for transaction in transactions:
        rows.append(transaction.to_row())
        color = manager.get_color(transaction.category)
        colors.append((row_number, "black", color))
        row_number = row_number + 1

    window["-TABLA-"].update(values=rows, row_colors=colors)
    window["-TITULO_TABLA-"].update(title)

    income = calculate_total_income(transactions)
    expenses = calculate_total_expenses(transactions)
    balance = calculate_balance(transactions)
    window["-TOTALES-"].update("Ingresos: " + format_colones(income) +
                                "    Gastos: " + format_colones(expenses) +
                                "    Balance: " + format_colones(balance))


def show_all(window, manager):
    window["-INICIO-"].update("")
    window["-FIN-"].update("")
    show_transactions(window, manager, manager.get_sorted_transactions(), "Todos los movimientos")


def show_deduction(amount):
    if amount == 0:
        return format_colones(0)
    return "- " + format_colones(amount)


def show_salary(window, config, year, month):
    pay_frequency = config.get_month_pay_frequency(year, month)
    monthly_salary = config.get_month(year, month)
    breakdown = config.calculate_breakdown(year, month)

  
    if pay_frequency == BIWEEKLY:
        window["-PAGO_MENSUAL-"].update(visible=False)
        window["-PAGO_IQ-"].update(visible=True)
        window["-PAGO_IIQ-"].update(visible=True)
        payment_names = [FIRST_FORTNIGHT, SECOND_FORTNIGHT]
    else:
        window["-PAGO_MENSUAL-"].update(visible=True)
        window["-PAGO_IQ-"].update(visible=False)
        window["-PAGO_IIQ-"].update(visible=False)
        payment_names = [MONTHLY]

 
    payments_text = ""
    pending = []
    for payment_name in payment_names:
        amount = None
        if monthly_salary is not None:
            amount = monthly_salary.get_amount(payment_name)
        if amount is None:
            payments_text = payments_text + payment_name + ": pendiente   "
            pending.append(payment_name)
        else:
            payments_text = payments_text + payment_name + ": " + format_colones(amount) + "   "

    if config.has_association():
        percentage = remove_decimals(config.association_percentage)
        association_text = "Asociación solidarista (" + str(percentage) + "%):"
    else:
        association_text = "Asociación solidarista (no aplica):"

    if len(pending) > 0:
        pending_text = "Falta ingresar: " + ", ".join(pending)
    else:
        pending_text = ""

    window["-TITULO_SALARIO-"].update("Salario de " + get_month_name(year, month))
    window["-MODALIDAD-"].update("Modalidad: " + pay_frequency)
    window["-PAGOS-"].update(payments_text)
    window["-BRUTO-"].update(format_colones(breakdown["bruto"]))
    window["-CCSS-"].update(show_deduction(breakdown["ccss"]))
    window["-RENTA-"].update(show_deduction(breakdown["renta"]))
    window["-TEXTO_ASOCIACION-"].update(association_text)
    window["-ASOCIACION-"].update(show_deduction(breakdown["asociacion"]))
    window["-TOTAL_REBAJOS-"].update(show_deduction(breakdown["total_rebajos"]))
    window["-NETO-"].update(format_colones(breakdown["neto"]))
    window["-PENDIENTES-"].update(pending_text)


def show_month(window, manager, config, year, month):
    window["-MES-"].update(value=MONTH_NAMES[month - 1])
    window["-ANIO-"].update(value=year)
    window["-INICIO-"].update("")
    window["-FIN-"].update("")
    title = "Movimientos de " + get_month_name(year, month)
    show_transactions(window, manager, manager.filter_by_month(year, month), title)
    show_salary(window, config, year, month)


def action_filter(window, manager, values):
    try:
        transactions = manager.filter_by_dates(values["-INICIO-"], values["-FIN-"])
    except ValueError as error:
        interfaces.show_error(str(error))
        return
    title = "Movimientos del " + values["-INICIO-"] + " al " + values["-FIN-"]
    show_transactions(window, manager, transactions, title)




def action_add_category(manager):
    window = interfaces.create_category_window()
    while True:
        event, values = window.read()
        if interfaces.was_closed(event):
            break
        if event == "-GUARDAR-":
            try:
                manager.add_category(values["-NOMBRE-"], values["-COLOR-"])
            except ValueError as error:
                interfaces.show_error(str(error))
                continue  
            save_manager(manager)
            break
    window.close()


def action_add_transaction(manager, transaction_type, year, month):
    if len(manager.categories) == 0:
        interfaces.show_error("No hay categorías disponibles. Agregue una categoría primero.")
        return None


    today = date.today()
    if year == today.year and month == today.month:
        date_value = today
    else:
        date_value = date(year, month, 1)

    window = interfaces.create_transaction_window(transaction_type, manager.get_category_names(),
                                                  date_value.strftime("%d/%m/%Y"))
    transaction = None
    while True:
        event, values = window.read()
        if interfaces.was_closed(event):
            break
        if event == "-GUARDAR-":
            try:
                transaction = manager.add_transaction(values["-TITULO-"], values["-MONTO-"],
                                                       values["-CATEGORIA-"], transaction_type, values["-FECHA-"])
            except ValueError as error:
                interfaces.show_error(str(error))
                continue
            save_manager(manager)
            break
    window.close()

    if transaction is not None:
        interfaces.show_message("Nuevo " + transaction_type.lower() + " agregado:\n" + str(transaction))
    return transaction


def action_export_csv(manager):
    if len(manager.transactions) == 0:
        interfaces.show_error("No hay movimientos para exportar.")
        return

    file_path = interfaces.ask_csv_path()
    if file_path is None or file_path == "":
        return

    transactions = manager.get_sorted_transactions()
    rows = []
    for transaction in transactions:
        rows.append(transaction.to_csv_row())

    totals = [
        "Totales:",
        "Ingresos: ₡" + str(remove_decimals(calculate_total_income(transactions))),
        "Gastos: ₡" + str(remove_decimals(calculate_total_expenses(transactions))),
        "Balance Neto: ₡" + str(remove_decimals(calculate_balance(transactions))),
    ]
    persistence.export_csv(file_path, rows, totals)
    interfaces.show_message("Archivo exportado en:\n" + file_path)




def action_configure_salary(config, year, month):
    is_biweekly = config.get_month_pay_frequency(year, month) == BIWEEKLY
    window = interfaces.create_config_window(is_biweekly, config.has_association(),
                                                     config.association_percentage,
                                                     get_month_name(year, month))
    was_saved = False
    while True:
        event, values = window.read()
        if interfaces.was_closed(event):
            break


        if event == "-SI-" or event == "-NO-":
            window["-PORCENTAJE-"].update(disabled=not values["-SI-"])

        if event == "-GUARDAR-":
            if values["-RADIO_QUINCENAL-"]:
                pay_frequency = BIWEEKLY
            else:
                pay_frequency = MONTHLY
            try:
                config.configure(pay_frequency, values["-SI-"], values["-PORCENTAJE-"], year, month)
            except ValueError as error:
                interfaces.show_error(str(error))
                continue
            save_salary(config)
            was_saved = True
            break

    window.close()
    return was_saved


def action_enter_payment(config, year, month, payment_name):
    monthly_salary = config.get_month(year, month)
    current_amount = None
    if monthly_salary is not None:
        current_amount = monthly_salary.get_amount(payment_name)

    if payment_name == MONTHLY:
        name = "salario mensual"
    else:
        name = payment_name

    message = ("Monto bruto de " + name + " de " + get_month_name(year, month) + " (₡)\n"
               "Incluya horas extra y comisiones, porque cuentan para el aguinaldo.")

    while True:
        text = interfaces.ask_amount(message, current_amount)
        if text is None: 
            return False
        try:
            config.register_payment(year, month, payment_name, text)
        except ValueError as error:
            interfaces.show_error(str(error))
            continue
        save_salary(config)
        return True


def show_christmas_bonus(window, config, year):
    result = calculate_christmas_bonus(config, year)

    if result["meses_registrados"] == 12:
        amount_label = "Aguinaldo total: " + format_colones(result["aguinaldo"])
    else:
        amount_label = "Aguinaldo acumulado: " + format_colones(result["aguinaldo"])

    window["-PERIODO-"].update("Periodo: del 01/12/" + str(year - 1) + " al 30/11/" + str(year))
    window["-TABLA_AGUINALDO-"].update(values=result["filas"])
    window["-TOTAL_BRUTO-"].update("Suma de salarios brutos: " + format_colones(result["total_bruto"]))
    window["-MESES_REGISTRADOS-"].update("Meses registrados: " + str(result["meses_registrados"]) + " de 12")
    window["-MONTO_AGUINALDO-"].update(amount_label)


def action_view_christmas_bonus(config):
    year = date.today().year
    window = interfaces.create_christmas_bonus_window(year)
    show_christmas_bonus(window, config, year)

    while True:
        event, values = window.read()
        if interfaces.was_closed(event):
            break
        if event == "-ANIO_AGUINALDO-":
            show_christmas_bonus(window, config, int(values["-ANIO_AGUINALDO-"]))

    window.close()
