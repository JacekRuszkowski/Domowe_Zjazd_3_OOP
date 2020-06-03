"""
Do zadania z klasą `Ogloszenie` dodaj kolejne kolejne klasy, które po niej dziedziczą.

`OgloszenieSamochodowe` – dziedziczy z `Ogloszenie` i dodatkowo określa cechy sprzedawanego samochodu jak model,
markę, rok produkcji, przebieg, pojemność, moc i rodzaj paliwa.
`OgloszenieMieszkaniowe` – też dziedziczy z `Ogloszenie`, a dodatkowo cechy sprzedawanego mieszkania
/ domu: miejscowość, metraż, liczba pokoi.

"""






class Advert:
    def __init__(self, title: str, price: float, contact: str):
        self.title = title
        self.price = price
        self.contact = contact

    def get_info(self):
        return f"Tytuł: {self.title}\nCena: {self.price} zł\nKontakt: {self.contact}"

    def __str__(self):
        return self.get_info()

class CarAdvert(Advert):
    def __init__(self, title: str, price: float, contact: str, mileage: int, year: int, fuel: str):
        super().__init__(title, price, contact)
        self.mileage = mileage
        self.year = year
        self.fuel = fuel

    def get_info(self):
        return f"Tytuł: {self.title}\nCena: {self.price} zł\nKontakt: {self.contact}\nPzebieg: {self.mileage}\n" \
               f"Rocznik: {self.year}\nRodzaj paliwa: {self.fuel} "



class HouseAdvert(Advert):
    def __init__(self, title: str, price: float, contact: str, location: str, size: float, rooms: int, amenities: str):
        super().__init__(title, price, contact)
        self.location = location
        self.size = size
        self.rooms = rooms
        self.amenities = amenities

    def get_info(self):
        return f"Tytuł: {self.title}\nCena: {self.price} zł\nKontakt: {self.contact}\nMiejscowość {self.location}\n" \
               f"Powierzchnia: {self.size} m kw.\nIlość pokoi: {self.rooms}\nUdogodnienia: {self.amenities} "






adv1 = Advert("Sprzedam Opla", 11000, "508 145 525")

adv2 = CarAdvert("Sprzedam Opla", 11000, "508 145 525", 150000, 2010, "Oil")

adv3 = HouseAdvert("Piękny dom rodzinny", 600000, "605 252 174", "Wrocław", 150, 6, "Blisko lasu. Dobry dojazd do centrum.")



print(adv3.get_info())




