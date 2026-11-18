from logic import format_colones, get_month_name


def get_christmas_bonus_months(year):
    months = [(year - 1, 12)]
    for month in range(1, 12):
        months.append((year, month))
    return months


def calculate_christmas_bonus(salary_config, year):
    rows = []
    total_gross = 0
    registered_months = 0

    for month_year, month in get_christmas_bonus_months(year):
        name = get_month_name(month_year, month)
        monthly_salary = salary_config.get_month(month_year, month)

        if monthly_salary is None:
            rows.append([name, "—", "Sin registrar"])
        else:
            gross = monthly_salary.get_gross_salary()
            total_gross = total_gross + gross
            registered_months = registered_months + 1

            if monthly_salary.is_complete():
                status = "Registrado"
            else:
                status = "Incompleto"
            rows.append([name, format_colones(gross), status])

    christmas_bonus = round(total_gross / 12, 2)

    return {
        "filas": rows,
        "total_bruto": total_gross,
        "meses_registrados": registered_months,
        "aguinaldo": christmas_bonus,
    }
