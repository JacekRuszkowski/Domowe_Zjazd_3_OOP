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
    ID = 1

    def __init__(self, product: str, price: float):
        self.product = product
        self.price = price
        self.added_products = []
        
    def get_info(self):
        return f"Produkt: {self.product}\nPrice: {self.price} zl"

    def __str__(self):
        return self.get_info()

class Basket:
    def __init__(self):
        self.products = []

    def add_products(self, product: Product()):
        self.products.append(product)

    # def generate_id(self):
    #     for Product.ID in self.added_products:
    #         Product.ID += 1
    #     return Product.ID

    # def id(self, id):
    #     for self.product in product_list:
    #         id += ID




pr1 = Product('Czekolada', 4.50)
pr2 = Product('Woda', 1.50)
pr3 = Product('Kanapka', 5.00)
pr4 = Product('Guma do żucia', 1.90)

basket = Basket.add_products(pr1)

# print(pr1.generate_id())
# print(pr2.generate_id())
# print(pr3.generate_id())

print(basket)

print(pr1.get_info())
