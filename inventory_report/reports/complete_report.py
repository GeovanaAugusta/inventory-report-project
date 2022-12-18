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
        # Counter({'Mendes': 2, 'Mendes LIMITED': 1, 'Men': 1})
        print(company_names)

        products = company_names.most_common()
        # Produto x quantidade, num array, [0] = nome, [1] = qnt
        # [({'Mendes, 2, 'Mendes LIMITED', 1, 'Men', 1})]
        # print(products)

        for product in products:
            # print(product)
            products_most_commons += f"- {product[0]}: {product[1]}\n"
            # print(products_most_commons)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company.replace(' LIMITED', '')}\n"
            f"Produtos estocados por empresa:\n"
            f"{products_most_commons}")

# SOURCE
# 2
# max and min in date
# https://stackoverflow.com/questions/28312482/max-date-in-python-list
# oldest = min(datetime_list)
# youngest = max(datetime_list)
# Pegar uma palavra que + se repita
# https://stackoverflow.com/questions/4131123/finding-the-most-frequent-character-in-a-string
# import collections
# s = "helloworld"
# print(collections.Counter(s).most_common(1)[0])
# Assim não passou no teste, então contando e usando o max resolveu
# https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item
# from collections import Counter
# z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
# Counter(z)
# Counter({'blue': 3, 'red': 2, 'yellow': 1})
# replace in python
# https://www.programiz.com/python-programming/methods/string/replace
# replaced_text = text.replace('b', 'c')
