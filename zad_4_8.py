"""
Zaimplementuj metodę statyczną tworzącą koszyk na podstawie listy podanych produktów.
Każdy z nich powinien zostać dodany do koszyka tylko raz.

Przykład użycia:
backset = Basket.with_products([prod_1, prod_2])
"""


class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def get_info(self) -> str:
        return f'Produkt "{self.name}", id: {self.id}, cena: {self.price:.2f} PLN'

    def __str__(self) -> str:
        return self.get_info()


class Basket:
    def __init__(self):
        self._items = dict()

    # metoda tworzy nowy koszyk z listy i produkcien(produkt dodawany jest raz, może zmieniać sie ilosć).
    @staticmethod
    def add_product(product_list: list):
        new_basket = dict()
        for product in product_list:
            if product not in new_basket:
                new_basket[product] = 1
            else:
                new_basket[product] += 1
        return new_basket
        # for product, amount in new_basket.items():
        #     print(f"{product}, Ilosć: {amount}")

    # czy do tej metody jest jakis dostęp z zewnątrz?

    def count_total_price(self) -> float:
        total_price = 0.0
        for product, quantity in self._items.items():
            total_price += product.price * quantity
        return total_price

    def generate_report(self):
        """
        Produkty w koszyku:
        - Woda (1), cena: 10.00 x 5
        W sumie: 50.00
        """
        print('Produkty w koszyku:')
        for product, quantity in self._items.items():
            print(f'- {product} x {quantity}')
        print(f'W sumie: {self.count_total_price():.2f} PLN')

    def product_count(self) -> int:
        return len(self._items)


b = Basket()
p1 = Product(1, 'Woda', 10.99)
p2 = Product(2, 'Pączek', 1.50)
p3 = Product(3, 'Jabłko', 2.70)
p4 = Product(4, 'Chipsy', 4.50)
p5 = Product(5, 'Koperta', 0.50)

koszyk = b.add_product([p1, p2, p3, p4, p4, p3, p2, p2, p5])
