### Zadanie 4.1 | Ogłoszenia

# Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia
# (takie jak w serwisie internetowym z ogłoszeniami).
# Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie,
# m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy.


class Advert:
    def __init__(self, title: str, price: float, description: str, contact: str):
        self.title = title
        self.price = price
        self.description = description
        self.contact = contact

    def get_info(self):
        return f"Tytuł: {self.title}\nCena: {self.price} zł\nOpis: {self.description}\nKontakt: {self.contact}"

    def __str__(self):
        return self.get_info()


adv1 = Advert("Sprzedam Opla", 11000, "sprzedam Opel Vectra - stan bezwypadkowy. Rocznik 2010", "508 145 525")

info = adv1.get_info()

print(info)


def test_sprawdzanie_danych():
    adv1 = Advert("Sprzedam Opla", 11000, "Sprzedam Opel Vectra - stan bezwypadkowy. Rocznik 2010", "508 145 525")
    assert adv1.title == "Sprzedam Opla"
    assert adv1.price == 11000
    assert adv1.description == "Sprzedam Opel Vectra - stan bezwypadkowy. Rocznik 2010"
    assert adv1.contact == "508 145 525"
