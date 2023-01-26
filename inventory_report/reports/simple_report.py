from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(productsList):

        oldest_date = min(
            [product["data_de_fabricacao"] for product in productsList]
        )

        closest_date = min([product["data_de_validade"]
                            for product in productsList])

        company_nm = max(
            Counter(product["nome_da_empresa"] for product in productsList))

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            # - Empresa com mais produtos: Correia LIMITED, remover o LIMITED
            f"Empresa com mais produtos: {company_nm.replace(' LIMITED', '')}")
