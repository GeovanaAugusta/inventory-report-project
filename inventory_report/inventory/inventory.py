from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    # 1 param caminho para o arquivo CSV e 2 o tipo de relatório
    def import_data(path, type):
        if "csv" in path:
            return Inventory.csv_path(path, type)
        elif "json" in path:
            return Inventory.json_path(path, type)

    @staticmethod
    def csv_path(path, type):
        with open(path, encoding="utf-8") as file:
            dic_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == "completo":
                return CompleteReport.generate(dic_reader)
            elif type == type == "simples":
                return SimpleReport.generate(list(dic_reader))

    @staticmethod
    def json_path(path, type):
        with open(path) as file:
            json_reader = json.load(file)
            if type == "simples":
                return SimpleReport.generate(json_reader)
            elif type == "completo":
                return CompleteReport.generate(json_reader)


# SOURCE
# 4
# https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/b436f9e0-dfde-4a16-9bad-82f0c559dd45/day/61e88b4a-b97a-4f96-b5a0-abaa50651e37/lesson/293603be-ede4-41d6-8921-963ecdb0bc44
# import csv

# with open("graduacao_unb.csv", encoding = "utf-8") as file:
#     graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
#     # Usando o conceito de desempacotamento
#     header, *data = graduacao_reader

#     with open(path, encoding="utf-8") as file:
        # dic_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        # return list(dic_reader)

# https://linuxhint.com/use-python-csv-dictreader/
# https://docs.python.org/3/library/csv.html

# JSON
# https://github.com/tryber/sd-020-a-inventory-report/pull/42/commits/ab266b0dfdd6a6d6d478188388eeb475cf0c3b16
# with open("pokemons.json") as file:
    # pokemons = json.load(file)["results"]
