import unittest

from aguinaldo import calcular_aguinaldo
from salario import ConfiguracionSalario, calcular_ccss, calcular_renta


class PruebasSalario(unittest.TestCase):

    def test_ccss_es_10_83_por_ciento(self):
        self.assertEqual(calcular_ccss(1000000), 108300)

    def test_renta_en_dos_tramos(self):
        self.assertEqual(calcular_renta(1500000), 65850)

    def test_salario_mensual_con_asociacion(self):
        configuracion = ConfiguracionSalario()
        configuracion.configurar("Mensual", True, "5", 2026, 11)
        configuracion.registrar_pago(2026, 11, "Mensual", "1500000")
        desglose = configuracion.calcular_desglose(2026, 11)
        self.assertEqual(desglose["ccss"], 162450)
        self.assertEqual(desglose["renta"], 65850)
        self.assertEqual(desglose["asociacion"], 75000)
        self.assertEqual(desglose["neto"], 1196700)

    def test_quincenal_suma_iq_e_iiq(self):
        configuracion = ConfiguracionSalario()
        configuracion.configurar("Quincenal", False, "", 2026, 11)
        configuracion.registrar_pago(2026, 11, "IQ", "750000")
        configuracion.registrar_pago(2026, 11, "IIQ", "750000")
        desglose = configuracion.calcular_desglose(2026, 11)
        self.assertEqual(desglose["bruto"], 1500000)
        self.assertEqual(desglose["renta"], 65850)  

    def test_cada_mes_tiene_su_salario(self):
        configuracion = ConfiguracionSalario()
        configuracion.registrar_pago(2026, 10, "Mensual", "1000000")
        configuracion.registrar_pago(2026, 11, "Mensual", "1200000")
        self.assertEqual(configuracion.calcular_desglose(2026, 10)["bruto"], 1000000)
        self.assertEqual(configuracion.calcular_desglose(2026, 11)["bruto"], 1200000)
        self.assertEqual(configuracion.obtener_mes(2026, 9), None)


class PruebasAguinaldo(unittest.TestCase):

    def test_aguinaldo_de_un_periodo_completo(self):
        configuracion = ConfiguracionSalario()
        configuracion.registrar_pago(2025, 12, "Mensual", "600000") 
        for mes in range(1, 12):                                       
            configuracion.registrar_pago(2026, mes, "Mensual", "600000")
        configuracion.registrar_pago(2026, 12, "Mensual", "999999") 

        resultado = calcular_aguinaldo(configuracion, 2026)
        self.assertEqual(resultado["meses_registrados"], 12)
        self.assertEqual(resultado["total_bruto"], 7200000)
        self.assertEqual(resultado["aguinaldo"], 600000)

    def test_aguinaldo_con_meses_faltantes(self):
        configuracion = ConfiguracionSalario()
        configuracion.configurar("Quincenal", False, "", 2026, 1)
        configuracion.registrar_pago(2026, 1, "IQ", "300000")
        configuracion.registrar_pago(2026, 1, "IIQ", "300000")
        configuracion.registrar_pago(2026, 2, "IQ", "300000")  

        resultado = calcular_aguinaldo(configuracion, 2026)
        self.assertEqual(resultado["meses_registrados"], 2)
        self.assertEqual(resultado["aguinaldo"], 75000)  
        self.assertEqual(resultado["filas"][2][2], "Incompleto") 


if __name__ == "__main__":
    unittest.main()
