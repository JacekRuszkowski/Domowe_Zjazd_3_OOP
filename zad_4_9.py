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

    def get_info(self):
        return f"Produkt: {self.product}\nPrice: {self.price} zl"

    def __str__(self):
        return self.get_info()

    def add_id(self):
        pass


class Basket:
    def __init__(self):
        self.basket = []

    def add_to_basket(self, product: Product):
        self.basket.append(product)

    def wyswietl_basket(self):
        for products in self.basket:
            Product.ID += 1
            print(f"{products}\nId: {Product.ID}\n")


pr1 = Product('Czekolada', 4.50)
pr2 = Product('Woda', 1.50)
pr3 = Product('Kanapka', 5.00)
pr4 = Product('Guma do żucia', 1.90)


basket = Basket()

basket.add_to_basket(pr1)
basket.add_to_basket(pr2)
basket.add_to_basket(pr3)
basket.add_to_basket(pr4)

print(basket.wyswietl_basket())
