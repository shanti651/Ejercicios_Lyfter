"""def ask_price():
    while True:
        try:
            precio = float(input("Cual es el precio del prodcuto?: "))
            break
        except ValueError:
            print("Escriba de nuevo el precio")
    return precio

def ask_percentage():
    while True:
        try:
            descuento = float(input("Cual es el descuento del prodcuto?: "))
            if descuento < 0 or descuento > 100:
                print("Error en descuento")
                continue
            break
        except ValueError:
            print("Escriba de nuevo el descuento")
    return descuento    


def apply_disccount(precio, percentage):
    new_price = precio - (precio * (percentage/100))
    return new_price

def show_result(original, final_price):
    print(f"El precio original es de {original}")
    print(f"El precio final es de {final_price}")
    print(f"Usted se ahorro {original-final_price}")

def main():
    precio = ask_price()
    descuento = ask_percentage()
    final_price = apply_disccount(precio, descuento)
    show_result(precio, final_price)

main()"""

prices = ["100", "50", "abc", "30"]
def convert_to_floats(price_list):
    new_list = []
    resultado = 0
    for x in price_list:
        try: 
            number = float(x)
            new_list.append(number)
        except ValueError:
            print(f"Invalid element: {x}")
    return new_list

def apply_tax_list(new_list, tax):
    impuesto_list = []
    for x in new_list:
        resultado = x + (x * (tax / 100))
        impuesto_list.append(resultado)
    return impuesto_list

def show_lists(original, converted, final):
    print(original)
    print(converted)
    print(final)

def main():
    converted = convert_to_floats(prices)       # Convertimos a float
    final = apply_tax_list(converted, 10)       # Aplicamos 10% de impuesto
    show_lists(prices, converted, final)

main()





        