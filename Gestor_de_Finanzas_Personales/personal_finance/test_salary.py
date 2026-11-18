import unittest

from christmas_bonus import calculate_christmas_bonus
from salary import SalaryConfig, calculate_ccss, calculate_income_tax


class SalaryTests(unittest.TestCase):

    def test_ccss_is_10_83_percent(self):
        self.assertEqual(calculate_ccss(1000000), 108300)

    def test_income_tax_in_two_brackets(self):
        self.assertEqual(calculate_income_tax(1500000), 65850)

    def test_monthly_salary_with_association(self):
        config = SalaryConfig()
        config.configure("Mensual", True, "5", 2026, 11)
        config.register_payment(2026, 11, "Mensual", "1500000")
        breakdown = config.calculate_breakdown(2026, 11)
        self.assertEqual(breakdown["ccss"], 162450)
        self.assertEqual(breakdown["renta"], 65850)
        self.assertEqual(breakdown["asociacion"], 75000)
        self.assertEqual(breakdown["neto"], 1196700)

    def test_biweekly_adds_iq_and_iiq(self):
        config = SalaryConfig()
        config.configure("Quincenal", False, "", 2026, 11)
        config.register_payment(2026, 11, "IQ", "750000")
        config.register_payment(2026, 11, "IIQ", "750000")
        breakdown = config.calculate_breakdown(2026, 11)
        self.assertEqual(breakdown["bruto"], 1500000)
        self.assertEqual(breakdown["renta"], 65850)  

    def test_each_month_has_its_own_salary(self):
        config = SalaryConfig()
        config.register_payment(2026, 10, "Mensual", "1000000")
        config.register_payment(2026, 11, "Mensual", "1200000")
        self.assertEqual(config.calculate_breakdown(2026, 10)["bruto"], 1000000)
        self.assertEqual(config.calculate_breakdown(2026, 11)["bruto"], 1200000)
        self.assertEqual(config.get_month(2026, 9), None)


class ChristmasBonusTests(unittest.TestCase):

    def test_christmas_bonus_full_period(self):
        config = SalaryConfig()
        config.register_payment(2025, 12, "Mensual", "600000") 
        for month in range(1, 12):                                       
            config.register_payment(2026, month, "Mensual", "600000")
        config.register_payment(2026, 12, "Mensual", "999999") 

        result = calculate_christmas_bonus(config, 2026)
        self.assertEqual(result["meses_registrados"], 12)
        self.assertEqual(result["total_bruto"], 7200000)
        self.assertEqual(result["aguinaldo"], 600000)

    def test_christmas_bonus_with_missing_months(self):
        config = SalaryConfig()
        config.configure("Quincenal", False, "", 2026, 1)
        config.register_payment(2026, 1, "IQ", "300000")
        config.register_payment(2026, 1, "IIQ", "300000")
        config.register_payment(2026, 2, "IQ", "300000")  

        result = calculate_christmas_bonus(config, 2026)
        self.assertEqual(result["meses_registrados"], 2)
        self.assertEqual(result["aguinaldo"], 75000)  
        self.assertEqual(result["filas"][2][2], "Incompleto") 


if __name__ == "__main__":
    unittest.main()
