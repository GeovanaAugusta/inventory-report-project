from inventory_report.inventory.product import Product


def mockedProduct():
    return Product(
        1,
        "Borracha",
        "Papelaria Solar",
        "2021-07-04",
        "2029-02-09",
        "FR48",
        "Ao abrigo de luz solar",
    )


def test_cria_produto():
    assert mockedProduct().id == 1
    assert mockedProduct().nome_do_produto == "Borracha"
    assert mockedProduct().nome_da_empresa == "Papelaria Solar"
    assert mockedProduct().data_de_fabricacao == "2021-07-04"
    assert mockedProduct().data_de_validade == "2029-02-09"
    assert mockedProduct().numero_de_serie == "FR48"
    assert mockedProduct().instrucoes_de_armazenamento == (
        "Ao abrigo de luz solar")


# SOURCE
# 1
# https://docs.pytest.org/en/7.1.x/how-to/assert.html
# content of test_assert1.py
# def f():
#     return 3


# def test_function():
#     assert f() == 4

# Quebrar linha
# https://w3.cs.jmu.edu/spragunr/CS240_F14/style_guide.shtml#:~:text=The%20preferred%20way%20of%20wrapping,a%20backslash%20for%20line%20continuation.
