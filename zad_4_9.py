"""
Zaimplementuj mechanizm automatycznego generowania kolejnych ID dla produktów.
Informację o kolejnym ID przechowuj jako pole klasowe (class attribute).

Przykład użycia:
> product_1 = Product('Woda', 1.99)
> product_1.id
1
> product_2 = Product('Chleb', 2.50)
> product_2.id
2

"""


class Product:
    ID = 0

    def __init__(self, product: str, price: float):
        self.product = product
        self.price = price
        Product.ID += 1
        self.id = Product.ID


    def get_info(self):
        return f"Produkt: {self.product}\nID: {self.id}\nPrice: {self.price} zl\n"

    def __str__(self):
        return self.get_info()


class Basket:
    def __init__(self):
        self._items = dict()

    # metoda tworzy nowy koszyk z listy i produkcien(produkt dosany jest raz, może zmieniać sie ilosć).
    @staticmethod
    def add_product(product_list: list):
        new_basket = dict()
        for product in product_list:
            if product not in new_basket:
                new_basket[product] = 1
            else:
                new_basket[product] += 1
        # return new_basket
        for product, amount in new_basket.items():
            print(f"{product}Ilosć: {amount}\n")
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
p1 = Product('Woda', 10.99)
p2 = Product('Pączek', 1.50)
p3 = Product('Jabłko', 2.70)
p4 = Product('Chipsy', 4.50)
p5 = Product('Koperta', 0.50)

koszyk = b.add_product([p1, p2, p3, p4, p4, p3, p2, p2, p5])
