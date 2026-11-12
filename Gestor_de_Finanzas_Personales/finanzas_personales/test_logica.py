import os
import unittest

import persistencia
from logica import GestorFinanzas, validar_fecha, validar_monto


def crear_gestor_de_prueba():
    gestor = GestorFinanzas()
    gestor.agregar_categoria("Trabajo", "#00FF00")
    gestor.agregar_categoria("Comida", "#FFA500")
    gestor.agregar_movimiento("Salario", "1000", "Trabajo", "Ingreso", "02/07/2025")
    gestor.agregar_movimiento("Pizza", "20", "Comida", "Gasto", "03/07/2025")
    gestor.agregar_movimiento("Ropa", "50", "Comida", "Gasto", "12/07/2025")
    return gestor


class PruebasLogica(unittest.TestCase):

    def test_monto_con_letras_da_error(self):
        with self.assertRaises(ValueError):
            validar_monto("mil")

    def test_fecha_con_formato_incorrecto_da_error(self):
        with self.assertRaises(ValueError):
            validar_fecha("2025-07-20")

    def test_fecha_futura_da_error(self):
        with self.assertRaises(ValueError):
            validar_fecha("01/01/2099")

    def test_no_permite_categorias_repetidas(self):
        gestor = GestorFinanzas()
        gestor.agregar_categoria("Comida", "")
        with self.assertRaises(ValueError):
            gestor.agregar_categoria("comida", "")

    def test_no_permite_movimientos_sin_categorias(self):
        gestor = GestorFinanzas()
        with self.assertRaises(ValueError):
            gestor.agregar_movimiento("Pizza", "20", "Comida", "Gasto", "03/07/2025")

    def test_totales_y_balance(self):
        gestor = crear_gestor_de_prueba()
        self.assertEqual(gestor.calcular_total_ingresos(gestor.movimientos), 1000)
        self.assertEqual(gestor.calcular_total_gastos(gestor.movimientos), 70)
        self.assertEqual(gestor.calcular_balance(gestor.movimientos), 930)

    def test_filtrar_por_fechas(self):
        gestor = crear_gestor_de_prueba()
        resultado = gestor.filtrar_por_fechas("01/07/2025", "10/07/2025")
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0].titulo, "Salario")
        self.assertEqual(resultado[1].titulo, "Pizza")

    def test_guardar_y_cargar_json(self):
        gestor = crear_gestor_de_prueba()
        persistencia.guardar_json(gestor.convertir_a_diccionario(), "prueba_datos.json")

        gestor_cargado = GestorFinanzas()
        gestor_cargado.cargar_desde_diccionario(persistencia.cargar_json("prueba_datos.json"))
        os.remove("prueba_datos.json")  

        self.assertEqual(len(gestor_cargado.movimientos), 3)
        self.assertEqual(gestor_cargado.obtener_color("Comida"), "#FFA500")


if __name__ == "__main__":
    unittest.main()
