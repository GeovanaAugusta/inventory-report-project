from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

mockedProduct = [
  {
    "id": 1,
    "nome_do_produto": "Borracha",
    "nome_da_empresa": "Papelaria Solar",
    "data_de_fabricacao": "2021-07-04",
    "data_de_validade": "2029-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Ao abrigo de luz solar"
  }
]


def test_decorar_relatorio():
    simple_report = ColoredReport(SimpleReport).generate(mockedProduct)
    complete_report = ColoredReport(CompleteReport).generate(mockedProduct)

    assert ("\033[31mPapelaria Solar\033[0m" in simple_report) is True
    assert ("\033[31mPapelaria Solar\033[0m" in complete_report) is True

    assert ("\033[32mData de fabricação mais antiga:\033[0m"
            in simple_report) is True
    assert ("\033[32mData de fabricação mais antiga:\033[0m"
            in complete_report) is True
    assert ("\033[32mData de validade mais próxima:\033[0m"
            in simple_report) is True
    assert ("\033[32mData de validade mais próxima:\033[0m"
            in complete_report) is True

    assert ("\033[36m2021-07-04\033[0m" in simple_report) is True
    assert ("\033[36m2021-07-04\033[0m" in complete_report) is True
    assert ("\033[36m2029-02-09\033[0m" in simple_report) is True
    assert ("\033[36m2029-02-09\033[0m" in complete_report) is True
