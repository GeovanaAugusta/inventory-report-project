from collections import Counter


class CompleteReport:
    @staticmethod
    def generate(productsList):

        oldest_date = min(
            [product["data_de_fabricacao"] for product in productsList]
        )

        closest_date = min([product["data_de_validade"]
                            for product in productsList])

        company = max(
            Counter(product["nome_da_empresa"] for product in productsList))

        products_most_commons = ""

        company_names = Counter(product["nome_da_empresa"]
                                for product in productsList)

        products = company_names.most_common()

        for product in products:

            products_most_commons += f"- {product[0]}: {product[1]}\n"

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company.replace(' LIMITED', '')}\n"
            f"Produtos estocados por empresa:\n"
            f"{products_most_commons}")
