import os
import unittest
import tempfile

import persistence
from logic import (FinanceManager, calculate_balance, calculate_total_expenses,
                   calculate_total_income, validate_amount, validate_date)


def create_test_manager():
    manager = FinanceManager()
    manager.add_category("Trabajo", "#00FF00")
    manager.add_category("Comida", "#FFA500")
    manager.add_transaction("Salario", "1000", "Trabajo", "Ingreso", "02/07/2025")
    manager.add_transaction("Pizza", "20", "Comida", "Gasto", "03/07/2025")
    manager.add_transaction("Ropa", "50", "Comida", "Gasto", "12/07/2025")
    return manager


class LogicTests(unittest.TestCase):

    def test_amount_with_letters_raises_error(self):
        with self.assertRaises(ValueError):
            validate_amount("mil")

    def test_date_with_wrong_format_raises_error(self):
        with self.assertRaises(ValueError):
            validate_date("2025-07-20")

    def test_future_date_raises_error(self):
        with self.assertRaises(ValueError):
            validate_date("01/01/2099")

    def test_duplicate_categories_not_allowed(self):
        manager = FinanceManager()
        manager.add_category("Comida", "")
        with self.assertRaises(ValueError):
            manager.add_category("comida", "")

    def test_transactions_without_categories_not_allowed(self):
        manager = FinanceManager()
        with self.assertRaises(ValueError):
            manager.add_transaction("Pizza", "20", "Comida", "Gasto", "03/07/2025")

    def test_totals_and_balance(self):
        manager = create_test_manager()
        self.assertEqual(calculate_total_income(manager.transactions), 1000)
        self.assertEqual(calculate_total_expenses(manager.transactions), 70)
        self.assertEqual(calculate_balance(manager.transactions), 930)

    def test_filter_by_dates(self):
        manager = create_test_manager()
        result = manager.filter_by_dates("01/07/2025", "10/07/2025")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].title, "Salario")
        self.assertEqual(result[1].title, "Pizza")

    def test_save_and_load_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = os.path.join(temp_dir, "prueba_datos.json")
            manager = create_test_manager()
            persistence.save_json(manager.to_dict(), test_file)

            loaded_manager = FinanceManager()
            loaded_manager.load_from_dict(persistence.load_json(test_file))

            self.assertEqual(len(loaded_manager.transactions), 3)
            self.assertEqual(loaded_manager.get_color("Comida"), "#FFA500")


if __name__ == "__main__":
    unittest.main()
