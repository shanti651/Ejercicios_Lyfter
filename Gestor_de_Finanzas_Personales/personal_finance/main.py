from datetime import date

import actions
import interfaces
from logic import EXPENSE, FIRST_FORTNIGHT, INCOME, MONTH_NAMES, MONTHLY, SECOND_FORTNIGHT
import os

def main():
    manager = actions.load_manager()
    config = actions.load_salary()

  
    today = date.today()
    year = today.year
    month = today.month


    if not os.path.exists("datos_salario.json"):
        actions.action_configure_salary(config, year, month)

    window = interfaces.create_main_window()
    actions.show_month(window, manager, config, year, month)

    while True:
        event, values = window.read()

        if interfaces.was_closed(event):
            break


        if event == "-MES-" or event == "-ANIO-":
            month = MONTH_NAMES.index(values["-MES-"]) + 1
            year = int(values["-ANIO-"])
            actions.show_month(window, manager, config, year, month)

        elif event == "-MES_ANTERIOR-":
            month = month - 1
            if month == 0:
                month = 12
                year = year - 1
            actions.show_month(window, manager, config, year, month)

        elif event == "-MES_SIGUIENTE-":
            month = month + 1
            if month == 13:
                month = 1
                year = year + 1
            actions.show_month(window, manager, config, year, month)


        elif event == "-AGREGAR_CATEGORIA-":
            actions.action_add_category(manager)

        elif event == "-AGREGAR_GASTO-" or event == "-AGREGAR_INGRESO-":
            if event == "-AGREGAR_GASTO-":
                transaction_type = EXPENSE
            else:
                transaction_type = INCOME
            transaction = actions.action_add_transaction(manager, transaction_type, year, month)
            if transaction is not None:
                year = transaction.date_value.year
                month = transaction.date_value.month
                actions.show_month(window, manager, config, year, month)

        elif event == "-FILTRAR-":
            actions.action_filter(window, manager, values)

        elif event == "-MOSTRAR_TODO-":
            actions.show_all(window, manager)

        elif event == "-EXPORTAR-":
            actions.action_export_csv(manager)

  
        elif event == "-CONFIGURAR-":
            if actions.action_configure_salary(config, year, month):
                actions.show_salary(window, config, year, month)

        elif event == "-PAGO_MENSUAL-" or event == "-PAGO_IQ-" or event == "-PAGO_IIQ-":
            if event == "-PAGO_MENSUAL-":
                payment_name = MONTHLY
            elif event == "-PAGO_IQ-":
                payment_name = FIRST_FORTNIGHT
            else:
                payment_name = SECOND_FORTNIGHT
            if actions.action_enter_payment(config, year, month, payment_name):
                actions.show_salary(window, config, year, month)

        elif event == "-AGUINALDO-":
            actions.action_view_christmas_bonus(config)


    actions.save_manager(manager)
    actions.save_salary(config)
    window.close()


if __name__ == "__main__":
    main()