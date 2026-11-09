from datetime import datetime, date

FORMATO_FECHA = "%d/%m/%Y"

NOMBRES_MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                 "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]




def convertir_texto_a_fecha(texto):
    try:
        fecha = datetime.strptime(texto.strip(), FORMATO_FECHA).date()
    except ValueError:
        raise ValueError("Formato de fecha inválido (use dd/mm/yyyy)")
    return fecha


def validar_fecha(texto):
    fecha = convertir_texto_a_fecha(texto)
    if fecha > date.today():
        raise ValueError("La fecha no puede ser en el futuro")
    return fecha


def validar_monto(texto):
    try:
        monto = float(texto)
    except ValueError:
        raise ValueError("El monto debe ser un número")
    if monto <= 0:
        raise ValueError("El monto debe ser mayor que cero")
    return monto


def validar_color(color):
    if color == "" or color == "None":
        return "#FFFFFF"

    if len(color) != 7 or color[0] != "#":
        raise ValueError("El color debe tener el formato #RRGGBB")

    for letra in color[1:]:
        if letra not in "0123456789abcdefABCDEF":
            raise ValueError("El color debe tener el formato #RRGGBB")

    return color.upper()


def formatear_colones(monto):
    return f"₡{monto:,.2f}"


def quitar_decimales(numero):
    if numero == int(numero):
        return int(numero)
    return numero


def obtener_nombre_mes(anio, mes):
    return NOMBRES_MESES[mes - 1] + " " + str(anio)


def obtener_fecha(movimiento):
    return movimiento.fecha




class Categoria:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color


class Movimiento:
    def __init__(self, titulo, monto, categoria, tipo, fecha):
        self.titulo = titulo
        self.monto = monto          
        self.categoria = categoria  
        self.tipo = tipo           
        self.fecha = fecha          

    def obtener_monto_con_signo(self):
        if self.tipo == "Gasto":
            return -self.monto
        return self.monto

    def obtener_fecha_texto(self):
        return self.fecha.strftime(FORMATO_FECHA)

    def convertir_a_fila(self):
        return [self.obtener_fecha_texto(), self.titulo,
                formatear_colones(self.obtener_monto_con_signo()), self.categoria, self.tipo]

    def convertir_a_fila_csv(self):
        return [self.obtener_fecha_texto(), self.titulo,
                quitar_decimales(self.obtener_monto_con_signo()), self.categoria, self.tipo]

    def convertir_a_diccionario(self):
        return {
            "fecha": self.obtener_fecha_texto(),
            "titulo": self.titulo,
            "monto": self.monto,
            "categoria": self.categoria,
            "tipo": self.tipo,
        }

    def __str__(self):
        return (f"Fecha: {self.obtener_fecha_texto()} | Título: {self.titulo} | "
                f"Monto: ₡{quitar_decimales(self.monto)} | Tipo: {self.tipo}")


class GestorFinanzas:
    def __init__(self):
        self.categorias = {}    
        self.movimientos = []   

 

    def agregar_categoria(self, nombre, color):
        nombre = nombre.strip()
        if nombre == "":
            raise ValueError("El nombre de la categoría es obligatorio")

        for nombre_existente in self.categorias:
            if nombre_existente.lower() == nombre.lower():
                raise ValueError("La categoría " + nombre + " ya existe")

        color = validar_color(color)
        self.categorias[nombre] = Categoria(nombre, color)

    def obtener_nombres_categorias(self):
        nombres = list(self.categorias.keys())
        nombres.sort()
        return nombres

    def obtener_color(self, nombre_categoria):
        if nombre_categoria in self.categorias:
            return self.categorias[nombre_categoria].color
        return "#FFFFFF"

 

    def agregar_movimiento(self, titulo, monto_texto, categoria, tipo, fecha_texto):
        if len(self.categorias) == 0:
            raise ValueError("No hay categorías disponibles. Agregue una categoría primero")

        titulo = titulo.strip()
        if titulo == "":
            raise ValueError("El título es obligatorio")

        monto = validar_monto(monto_texto)

        if categoria not in self.categorias:
            raise ValueError("Debe elegir una categoría")

        fecha = validar_fecha(fecha_texto)

        movimiento = Movimiento(titulo, monto, categoria, tipo, fecha)
        self.movimientos.append(movimiento)
        return movimiento

    def obtener_movimientos_ordenados(self):
        return sorted(self.movimientos, key=obtener_fecha)

    def filtrar_por_fechas(self, inicio_texto, fin_texto):
        inicio = convertir_texto_a_fecha(inicio_texto)
        fin = convertir_texto_a_fecha(fin_texto)
        if inicio > fin:
            raise ValueError("La fecha de inicio no puede ser mayor que la fecha de fin")

        resultado = []
        for movimiento in self.obtener_movimientos_ordenados():
            if movimiento.fecha >= inicio and movimiento.fecha <= fin:
                resultado.append(movimiento)
        return resultado

    def filtrar_por_mes(self, anio, mes):
        resultado = []
        for movimiento in self.obtener_movimientos_ordenados():
            if movimiento.fecha.year == anio and movimiento.fecha.month == mes:
                resultado.append(movimiento)
        return resultado



    def calcular_total_ingresos(self, movimientos):
        total = 0
        for movimiento in movimientos:
            if movimiento.tipo == "Ingreso":
                total = total + movimiento.monto
        return total

    def calcular_total_gastos(self, movimientos):
        total = 0
        for movimiento in movimientos:
            if movimiento.tipo == "Gasto":
                total = total + movimiento.monto
        return total

    def calcular_balance(self, movimientos):
        return self.calcular_total_ingresos(movimientos) - self.calcular_total_gastos(movimientos)

   

    def convertir_a_diccionario(self):
        categorias = {}
        for nombre in self.categorias:
            categorias[nombre] = self.categorias[nombre].color

        movimientos = []
        for movimiento in self.movimientos:
            movimientos.append(movimiento.convertir_a_diccionario())

        return {"categorias": categorias, "movimientos": movimientos}

    def cargar_desde_diccionario(self, datos):
        for nombre in datos["categorias"]:
            self.categorias[nombre] = Categoria(nombre, datos["categorias"][nombre])

        for dato in datos["movimientos"]:
            fecha = convertir_texto_a_fecha(dato["fecha"])
            monto = abs(dato["monto"])  
            movimiento = Movimiento(dato["titulo"], monto, dato["categoria"], dato["tipo"], fecha)
            self.movimientos.append(movimiento)
