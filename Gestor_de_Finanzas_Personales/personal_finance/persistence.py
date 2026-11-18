import csv
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FINANCE_FILE = os.path.join(BASE_DIR, "datos_finanzas.json")
SALARY_FILE = os.path.join(BASE_DIR, "datos_salario.json")


def save_json(data, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_json(file_name):
    if not os.path.exists(file_name):
        return None

    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def export_csv(file_path, rows, total_lines):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha", "Título", "Monto", "Categoría", "Tipo"])
        for row in rows:
            writer.writerow(row)
        writer.writerow([])
        for line in total_lines:
            writer.writerow([line])
