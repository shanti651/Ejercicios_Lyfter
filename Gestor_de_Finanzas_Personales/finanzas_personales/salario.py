from logica import validar_monto


PORCENTAJE_CCSS = 10.83


def calcular_ccss(salario_bruto):
    return round(salario_bruto * PORCENTAJE_CCSS / 100, 2)


def calcular_renta(salario_bruto):
    impuesto = 0
    salario = salario_bruto

    if salario > 4727000:
        impuesto = impuesto + (salario - 4727000) * 0.25
        salario = 4727000

    if salario > 2364000:
        impuesto = impuesto + (salario - 2364000) * 0.20
        salario = 2364000

    if salario > 1347000:
        impuesto = impuesto + (salario - 1347000) * 0.15
        salario = 1347000

    if salario > 918000:
        impuesto = impuesto + (salario - 918000) * 0.10

    return round(impuesto, 2)


def calcular_asociacion(salario_bruto, porcentaje):
    return round(salario_bruto * porcentaje / 100, 2)


def validar_porcentaje(texto):
    try:
        porcentaje = float(texto)
    except ValueError:
        raise ValueError("El porcentaje de la asociación debe ser un número")
    if porcentaje <= 0 or porcentaje > 100:
        raise ValueError("El porcentaje de la asociación debe estar entre 0 y 100")
    return porcentaje


class SalarioMes:

    def __init__(self, anio, mes, modalidad):
        self.anio = anio
        self.mes = mes
        self.modalidad = modalidad  
        self.pagos = {}            

    def agregar_pago(self, nombre_pago, monto):
        if self.modalidad == "Mensual" and nombre_pago != "Mensual":
            raise ValueError("Este mes es mensual, no tiene quincenas")
        if self.modalidad == "Quincenal" and nombre_pago == "Mensual":
            raise ValueError("Este mes es quincenal, ingrese la IQ o la IIQ")
        self.pagos[nombre_pago] = monto

    def obtener_monto(self, nombre_pago):
        if nombre_pago in self.pagos:
            return self.pagos[nombre_pago]
        return None

    def obtener_salario_bruto(self):
        total = 0
        for nombre_pago in self.pagos:
            total = total + self.pagos[nombre_pago]
        return total

    def obtener_pagos_pendientes(self):
        if self.modalidad == "Mensual":
            necesarios = ["Mensual"]
        else:
            necesarios = ["IQ", "IIQ"]

        pendientes = []
        for nombre_pago in necesarios:
            if nombre_pago not in self.pagos:
                pendientes.append(nombre_pago)
        return pendientes

    def esta_completo(self):
        return len(self.obtener_pagos_pendientes()) == 0

    def convertir_a_diccionario(self):
        return {"anio": self.anio, "mes": self.mes, "modalidad": self.modalidad, "pagos": self.pagos}


class ConfiguracionSalario:


    def __init__(self):
        self.modalidad = "Mensual"
        self.porcentaje_asociacion = 0   
        self.meses = {}                  

    def crear_clave(self, anio, mes):
        return str(anio) + "-" + str(mes)

    def tiene_asociacion(self):
        return self.porcentaje_asociacion > 0

    def configurar(self, modalidad, tiene_asociacion, porcentaje_texto, anio, mes):
        if tiene_asociacion:
            porcentaje = validar_porcentaje(porcentaje_texto)
        else:
            porcentaje = 0

  
        clave = self.crear_clave(anio, mes)
        if clave in self.meses and self.meses[clave].modalidad != modalidad:
            del self.meses[clave]

        self.modalidad = modalidad
        self.porcentaje_asociacion = porcentaje

    def obtener_mes(self, anio, mes):
        clave = self.crear_clave(anio, mes)
        if clave in self.meses:
            return self.meses[clave]
        return None

    def obtener_modalidad_del_mes(self, anio, mes):
        salario_mes = self.obtener_mes(anio, mes)
        if salario_mes is None:
            return self.modalidad
        return salario_mes.modalidad

    def registrar_pago(self, anio, mes, nombre_pago, monto_texto):
        monto = validar_monto(monto_texto)

        salario_mes = self.obtener_mes(anio, mes)
        if salario_mes is None:
            salario_mes = SalarioMes(anio, mes, self.modalidad)

        salario_mes.agregar_pago(nombre_pago, monto)
        self.meses[self.crear_clave(anio, mes)] = salario_mes

    def calcular_desglose(self, anio, mes):
        salario_mes = self.obtener_mes(anio, mes)
        if salario_mes is None:
            bruto = 0
        else:
            bruto = salario_mes.obtener_salario_bruto()

        ccss = calcular_ccss(bruto)
        renta = calcular_renta(bruto)
        asociacion = calcular_asociacion(bruto, self.porcentaje_asociacion)
        total_rebajos = round(ccss + renta + asociacion, 2)
        neto = round(bruto - total_rebajos, 2)

        return {
            "bruto": bruto,
            "ccss": ccss,
            "renta": renta,
            "asociacion": asociacion,
            "total_rebajos": total_rebajos,
            "neto": neto,
        }

 

    def convertir_a_diccionario(self):
        lista_meses = []
        for clave in self.meses:
            lista_meses.append(self.meses[clave].convertir_a_diccionario())

        return {
            "modalidad": self.modalidad,
            "porcentaje_asociacion": self.porcentaje_asociacion,
            "meses": lista_meses,
        }

    def cargar_desde_diccionario(self, datos):
        self.modalidad = datos["modalidad"]
        self.porcentaje_asociacion = datos["porcentaje_asociacion"]

        for dato_mes in datos["meses"]:
            salario_mes = SalarioMes(dato_mes["anio"], dato_mes["mes"], dato_mes["modalidad"])
            salario_mes.pagos = dato_mes["pagos"]
            self.meses[self.crear_clave(dato_mes["anio"], dato_mes["mes"])] = salario_mes
