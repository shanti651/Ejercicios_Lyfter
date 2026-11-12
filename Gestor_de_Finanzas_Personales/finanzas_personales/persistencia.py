import csv
import json
import os

ARCHIVO_FINANZAS = "datos_finanzas.json"
ARCHIVO_SALARIO = "datos_salario.json"


def guardar_json(datos, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)


def cargar_json(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return None

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def exportar_csv(ruta, filas, lineas_totales):
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Fecha", "Título", "Monto", "Categoría", "Tipo"])
        for fila in filas:
            escritor.writerow(fila)
        for linea in lineas_totales:
            escritor.writerow([linea])
