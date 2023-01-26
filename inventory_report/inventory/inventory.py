from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def import_data(path, type):
        if "csv" in path:
            return Inventory.csv_path(path, type)
        elif "json" in path:
            return Inventory.json_path(path, type)

    @staticmethod
    def csv_path(path, type):
        with open(path, encoding="utf-8") as file:
            dic_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == "simples":
                return SimpleReport.generate(list(dic_reader))
            elif type == "completo":
                return CompleteReport.generate(list(dic_reader))

    @staticmethod
    def json_path(path, type):
        with open(path) as file:
            json_reader = json.load(file)
            if type == "simples":
                return SimpleReport.generate(json_reader)
            elif type == "completo":
                return CompleteReport.generate(json_reader)
