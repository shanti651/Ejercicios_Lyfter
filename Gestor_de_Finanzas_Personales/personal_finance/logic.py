from datetime import datetime, date

DATE_FORMAT = "%d/%m/%Y"

MONTH_NAMES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                 "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

EXPENSE = "Gasto"
INCOME = "Ingreso"
TRANSACTION_TYPES = (EXPENSE, INCOME)

MONTHLY = "Mensual"
BIWEEKLY = "Quincenal"
FIRST_FORTNIGHT = "IQ"
SECOND_FORTNIGHT = "IIQ"
PAY_FREQUENCIES = (MONTHLY, BIWEEKLY)




def parse_date(text):
    try:
        date_value = datetime.strptime(text.strip(), DATE_FORMAT).date()
    except ValueError:
        raise ValueError("Formato de fecha inválido (use dd/mm/yyyy)")
    return date_value


def validate_date(text):
    date_value = parse_date(text)
    if date_value > date.today():
        raise ValueError("La fecha no puede ser en el futuro")
    return date_value


def validate_amount(text):
    try:
        amount = float(text)
    except ValueError:
        raise ValueError("El monto debe ser un número")
    if amount <= 0:
        raise ValueError("El monto debe ser mayor que cero")
    return amount


def validate_color(color):
    if color == "" or color == "None":
        return "#FFFFFF"

    if len(color) != 7 or color[0] != "#":
        raise ValueError("El color debe tener el formato #RRGGBB")

    for char in color[1:]:
        if char not in "0123456789abcdefABCDEF":
            raise ValueError("El color debe tener el formato #RRGGBB")

    return color.upper()


def format_colones(amount):
    return f"₡{amount:,.2f}"


def remove_decimals(number):
    if number == int(number):
        return int(number)
    return number


def get_month_name(year, month):
    return MONTH_NAMES[month - 1] + " " + str(year)


def get_date(transaction):
    return transaction.date_value


def calculate_total_income(transactions):
    total = 0
    for transaction in transactions:
        if transaction.transaction_type == INCOME:
            total = total + transaction.amount
    return total


def calculate_total_expenses(transactions):
    total = 0
    for transaction in transactions:
        if transaction.transaction_type == EXPENSE:
            total = total + transaction.amount
    return total


def calculate_balance(transactions):
    return calculate_total_income(transactions) - calculate_total_expenses(transactions)




class Category:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Transaction:
    def __init__(self, title, amount, category, transaction_type, date_value):
        self.title = title
        self.amount = amount          
        self.category = category  
        self.transaction_type = transaction_type           
        self.date_value = date_value          

    def get_signed_amount(self):
        if self.transaction_type == EXPENSE:
            return -self.amount
        return self.amount

    def get_date_text(self):
        return self.date_value.strftime(DATE_FORMAT)

    def to_row(self):
        return [self.get_date_text(), self.title,
                format_colones(self.get_signed_amount()), self.category, self.transaction_type]

    def to_csv_row(self):
        return [self.get_date_text(), self.title,
                remove_decimals(self.get_signed_amount()), self.category, self.transaction_type]

    def to_dict(self):
        return {
            "fecha": self.get_date_text(),
            "titulo": self.title,
            "monto": self.amount,
            "categoria": self.category,
            "tipo": self.transaction_type,
        }

    def __str__(self):
        return (f"Fecha: {self.get_date_text()} | Título: {self.title} | "
                f"Monto: ₡{remove_decimals(self.amount)} | Tipo: {self.transaction_type}")


class FinanceManager:
    def __init__(self):
        self.categories = {}    
        self.transactions = []   

 

    def add_category(self, name, color):
        name = name.strip()
        if name == "":
            raise ValueError("El nombre de la categoría es obligatorio")

        for existing_name in self.categories:
            if existing_name.lower() == name.lower():
                raise ValueError("La categoría " + name + " ya existe")

        color = validate_color(color)
        self.categories[name] = Category(name, color)

    def get_category_names(self):
        names = list(self.categories.keys())
        names.sort()
        return names

    def get_color(self, category_name):
        if category_name in self.categories:
            return self.categories[category_name].color
        return "#FFFFFF"

 

    def add_transaction(self, title, amount_text, category, transaction_type, date_text):
        if transaction_type not in TRANSACTION_TYPES:
            raise ValueError("Tipo de movimiento inválido: " + str(transaction_type) +
                             ". Debe ser " + EXPENSE + " o " + INCOME)

        if len(self.categories) == 0:
            raise ValueError("No hay categorías disponibles. Agregue una categoría primero")

        title = title.strip()
        if title == "":
            raise ValueError("El título es obligatorio")

        amount = validate_amount(amount_text)

        if category not in self.categories:
            raise ValueError("Debe elegir una categoría")

        date_value = validate_date(date_text)

        transaction = Transaction(title, amount, category, transaction_type, date_value)
        self.transactions.append(transaction)
        return transaction

    def get_sorted_transactions(self):
        return sorted(self.transactions, key=get_date)

    def filter_by_dates(self, start_text, end_text):
        start = parse_date(start_text)
        end = parse_date(end_text)
        if start > end:
            raise ValueError("La fecha de inicio no puede ser mayor que la fecha de fin")

        result = []
        for transaction in self.get_sorted_transactions():
            if transaction.date_value >= start and transaction.date_value <= end:
                result.append(transaction)
        return result

    def filter_by_month(self, year, month):
        result = []
        for transaction in self.get_sorted_transactions():
            if transaction.date_value.year == year and transaction.date_value.month == month:
                result.append(transaction)
        return result



    def to_dict(self):
        categories = {}
        for name in self.categories:
            categories[name] = self.categories[name].color

        transactions = []
        for transaction in self.transactions:
            transactions.append(transaction.to_dict())

        return {"categorias": categories, "movimientos": transactions}

    def load_from_dict(self, data):
        for name in data["categorias"]:
            self.categories[name] = Category(name, data["categorias"][name])

        for item in data["movimientos"]:
            date_value = parse_date(item["fecha"])
            amount = abs(item["monto"])  
            transaction = Transaction(item["titulo"], amount, item["categoria"], item["tipo"], date_value)
            self.transactions.append(transaction)
