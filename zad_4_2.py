"""
### Zadanie 4.2 | Lista ogłoszeń

Napisz programy, w których tworzysz listę ogłoszeń samochodowych, a następnie wyszukujesz ogłoszenia na podstawie
ich parametrów.

Na przykład ogłoszenia o cenach z określonego przedziału.

Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać wyszukane. Użyj poznanych kolekcji do trzymania
ogłoszeń. Możesz zastosować metodę `filter` do wyszukiwania odpowiednich ogłoszeń.

"""


class Advert:
    def __init__(self, title: str, price: float, contact: str):
        self.title = title
        self.price = price
        self.contact = contact

    def get_info(self):
        return f"Tytuł: {self.title}, Cena: {self.price} zł, Kontakt: {self.contact}"

    def __str__(self):
        return self.get_info()


class AdvertsList:
    def __init__(self):
        self.elements = []

    def add_advert(self, advert: Advert):
        self.elements.append(advert)

    def list_lenght(self):
        return len(self.elements)

    # wypisanie wszystkich ogłoszeń

    def wypisz(self):
        print("Aktualne ogłeszenia:")
        for elements in self.elements:
            print(elements)

    # szukanie w przedziale cenowym bez funckji lambda
    # def search_price_range(self, start, end):
    #     for searched in self.elements:
    #         if start < searched.price < end:
    #             print(searched)

    # szukanie w przedziale cenowym z funkcją lambda
    def search_price_range(self, start, end):
        print(f"Znalezione ogłosznia w podanym przedziale:")
        searched = list(filter(lambda searched_price: start < searched_price.price < end, self.elements))
        for found in searched:
            print(found)


adv1 = Advert("Opel Vectra", 11000, "508 145 525")
adv2 = Advert("Subaru forester", 35000, "503 206 400")
adv3 = Advert("Honda Civic", 15000, "500 658 898")
adv4 = Advert("Mitsubishi ASX", 45300, "605 654 123")
adv5 = Advert("Ford Mondeo", 33000, "603 562 980")
adv6 = Advert("Renault Megane", 23000, "603 562 980")

ogloszenia = AdvertsList()
ogloszenia.add_advert(adv1)
ogloszenia.add_advert(adv2)
ogloszenia.add_advert(adv3)
ogloszenia.add_advert(adv4)
ogloszenia.add_advert(adv5)
ogloszenia.add_advert(adv6)

print(ogloszenia.wypisz())
print()
print(ogloszenia.search_price_range(15000, 40000))


#  PYTANIA #
# 1. Dlaczego wypisuje mi none na końcu?
# 2. Dlaczego w metodzie "wypisz" jak daję print(elements) to wypisuje mi wszystskie,
#    a jak daję return elements to wypisuje mi tylko pierszy z pętlli?

# TESTY

def test_add_advert():
    adv1 = Advert("Opel Vectra", 11000, "508 145 525")
    adv2 = Advert("Subaru forester", 35000, "503 206 400")
    ogloszenia = AdvertsList()
    ogloszenia.add_advert(adv1)
    ogloszenia.add_advert(adv2)
    assert ogloszenia.list_lenght() == 2


def test_search():
    adv1 = Advert("Opel Vectra", 11000, "508 145 525")
    adv2 = Advert("Subaru forester", 35000, "503 206 400")
    ogloszenia = AdvertsList()
    ogloszenia.add_advert(adv1)
    ogloszenia.add_advert(adv2)
    assert ogloszenia.search_price_range(4000, 7000) == None
