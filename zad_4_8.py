"""
Zaimplementuj metodę statyczną tworzącą koszyk na podstawie listy podanych produktów.
Każdy z nich powinien zostać dodany do koszyka tylko raz.

Przykład użycia:
backset = Basket.with_products([prod_1, prod_2])
"""


class Basket:
    @staticmethod
    def add_product(product_list):
        added_products = []
        for product in product_list:
            if not product in added_products:
                added_products.append(product)
        return added_products


basket = Basket.add_product(["p1", "p1", "p2", "p3", "p4", "p1"])
print(basket)


def test_dodanie_produktow():
    assert Basket.add_product(["product_1", "product_2", "product_3", "product_4"]) == ["product_1",
                                                                                        "product_2",
                                                                                        "product_3",
                                                                                        "product_4"]


def test_dodanie_tego_samego():
    assert Basket.add_product(["product_1", "product_2", "product_1", "product_3", "product_2"]) == ["product_1",
                                                                                                     "product_2",
                                                                                                     "product_3"]
