from logic import BIWEEKLY, FIRST_FORTNIGHT, MONTHLY, SECOND_FORTNIGHT, validate_amount


CCSS_PERCENTAGE = 10.83


def calculate_ccss(gross_salary):
    return round(gross_salary * CCSS_PERCENTAGE / 100, 2)


def calculate_income_tax(gross_salary):
    tax = 0
    salary = gross_salary

    if salary > 4727000:
        tax = tax + (salary - 4727000) * 0.25
        salary = 4727000

    if salary > 2364000:
        tax = tax + (salary - 2364000) * 0.20
        salary = 2364000

    if salary > 1347000:
        tax = tax + (salary - 1347000) * 0.15
        salary = 1347000

    if salary > 918000:
        tax = tax + (salary - 918000) * 0.10

    return round(tax, 2)


def calculate_association(gross_salary, percentage):
    return round(gross_salary * percentage / 100, 2)


def validate_percentage(text):
    try:
        percentage = float(text)
    except ValueError:
        raise ValueError("El porcentaje de la asociación debe ser un número")
    if percentage <= 0 or percentage > 100:
        raise ValueError("El porcentaje de la asociación debe estar entre 0 y 100")
    return percentage


class MonthlySalary:

    def __init__(self, year, month, pay_frequency):
        self.year = year
        self.month = month
        self.pay_frequency = pay_frequency  
        self.payments = {}            

    def add_payment(self, payment_name, amount):
        if self.pay_frequency == MONTHLY and payment_name != MONTHLY:
            raise ValueError("Este mes es mensual, no tiene quincenas")
        if self.pay_frequency == BIWEEKLY and payment_name == MONTHLY:
            raise ValueError("Este mes es quincenal, ingrese la IQ o la IIQ")
        self.payments[payment_name] = amount

    def get_amount(self, payment_name):
        if payment_name in self.payments:
            return self.payments[payment_name]
        return None

    def get_gross_salary(self):
        total = 0
        for payment_name in self.payments:
            total = total + self.payments[payment_name]
        return total

    def get_pending_payments(self):
        if self.pay_frequency == MONTHLY:
            required = [MONTHLY]
        else:
            required = [FIRST_FORTNIGHT, SECOND_FORTNIGHT]

        pending = []
        for payment_name in required:
            if payment_name not in self.payments:
                pending.append(payment_name)
        return pending

    def is_complete(self):
        return len(self.get_pending_payments()) == 0

    def to_dict(self):
        return {"anio": self.year, "mes": self.month, "modalidad": self.pay_frequency, "pagos": self.payments}


class SalaryConfig:


    def __init__(self):
        self.pay_frequency = MONTHLY
        self.association_percentage = 0   
        self.months = {}                  

    def make_key(self, year, month):
        return str(year) + "-" + str(month)

    def has_association(self):
        return self.association_percentage > 0

    def configure(self, pay_frequency, has_association, percentage_text, year, month):
        if has_association:
            percentage = validate_percentage(percentage_text)
        else:
            percentage = 0

  
        key = self.make_key(year, month)
        if key in self.months and self.months[key].pay_frequency != pay_frequency:
            del self.months[key]

        self.pay_frequency = pay_frequency
        self.association_percentage = percentage

    def get_month(self, year, month):
        key = self.make_key(year, month)
        if key in self.months:
            return self.months[key]
        return None

    def get_month_pay_frequency(self, year, month):
        monthly_salary = self.get_month(year, month)
        if monthly_salary is None:
            return self.pay_frequency
        return monthly_salary.pay_frequency

    def register_payment(self, year, month, payment_name, amount_text):
        amount = validate_amount(amount_text)

        monthly_salary = self.get_month(year, month)
        if monthly_salary is None:
            monthly_salary = MonthlySalary(year, month, self.pay_frequency)

        monthly_salary.add_payment(payment_name, amount)
        self.months[self.make_key(year, month)] = monthly_salary

    def calculate_breakdown(self, year, month):
        monthly_salary = self.get_month(year, month)
        if monthly_salary is None:
            gross = 0
        else:
            gross = monthly_salary.get_gross_salary()

        ccss = calculate_ccss(gross)
        income_tax = calculate_income_tax(gross)
        association = calculate_association(gross, self.association_percentage)
        total_deductions = round(ccss + income_tax + association, 2)
        net = round(gross - total_deductions, 2)

        return {
            "bruto": gross,
            "ccss": ccss,
            "renta": income_tax,
            "asociacion": association,
            "total_rebajos": total_deductions,
            "neto": net,
        }

 

    def to_dict(self):
        month_list = []
        for key in self.months:
            month_list.append(self.months[key].to_dict())

        return {
            "modalidad": self.pay_frequency,
            "porcentaje_asociacion": self.association_percentage,
            "meses": month_list,
        }

    def load_from_dict(self, data):
        self.pay_frequency = data["modalidad"]
        self.association_percentage = data["porcentaje_asociacion"]

        for month_data in data["meses"]:
            monthly_salary = MonthlySalary(month_data["anio"], month_data["mes"], month_data["modalidad"])
            monthly_salary.payments = month_data["pagos"]
            self.months[self.make_key(month_data["anio"], month_data["mes"])] = monthly_salary
