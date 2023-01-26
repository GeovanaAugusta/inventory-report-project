from inventory_report.inventory.product import Product


def mockedProduct():
    return Product(
        1,
        "Borracha",
        "Papelaria Solar",
        "2021-07-04",
        "2029-02-09",
        "FR48",
        "ao abrigo de luz solar",
    )


def test_relatorio_produto():

    assert mockedProduct().__str__() == (
        "O produto Borracha"
        " fabricado em 2021-07-04"
        " por Papelaria Solar com validade"
        " até 2029-02-09"
        " precisa ser armazenado ao abrigo de luz solar."
    )
