from logica import formatear_colones, obtener_nombre_mes


def obtener_meses_del_aguinaldo(anio):
    meses = [(anio - 1, 12)]
    for mes in range(1, 12):
        meses.append((anio, mes))
    return meses


def calcular_aguinaldo(configuracion_salario, anio):
    filas = []
    total_bruto = 0
    meses_registrados = 0

    for anio_del_mes, mes in obtener_meses_del_aguinaldo(anio):
        nombre = obtener_nombre_mes(anio_del_mes, mes)
        salario_mes = configuracion_salario.obtener_mes(anio_del_mes, mes)

        if salario_mes is None:
            filas.append([nombre, "—", "Sin registrar"])
        else:
            bruto = salario_mes.obtener_salario_bruto()
            total_bruto = total_bruto + bruto
            meses_registrados = meses_registrados + 1

            if salario_mes.esta_completo():
                estado = "Registrado"
            else:
                estado = "Incompleto"
            filas.append([nombre, formatear_colones(bruto), estado])

    aguinaldo = round(total_bruto / 12, 2)

    return {
        "filas": filas,
        "total_bruto": total_bruto,
        "meses_registrados": meses_registrados,
        "aguinaldo": aguinaldo,
    }
