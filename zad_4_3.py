"""Stwórz klasę `Pociag`. Klasa niech ma dwa atrybuty: predkość (początkowa wartość to 10) i ilosc_paliwa
(początkowa wartość to 1000).
​
Dodaj do klasy `Pociag` metode `opis`. Ta metoda niech zwraca napis o treści "Moja predkość to (ileś tam)." \
                                                                              "Mam jeszcze (ileś tam) litrów paliwa."
Dodatkowo zaimplementuj metodę `__str__`.
​
Dodaj metode `przyspiesz`. Ta metoda niech przyjmuje jeden argument mówiący, o ile ma zwiekszyć się prędkość. Ta metoda
niech zwiększa predkość pociągu o tyle, ile jest powiedziane w argumencie. I niech zmniejsza ilość paliwa o:
`(nowa predkosc - stara_predkosc) * (stara predkosc / 100)`.
​
Niech nie da się jednorazowo zwiększyć prędkości o więcej niż 75% (jeśli ktoś spróbuje tak zwiększyć prędkość, prędkość
niech pozostaje po prostu bez zmian). Niech nie da sie zwiększyć prędkości, jeśli pociąg nie ma juz paliwa (jeśli ktoś
spróbuje zwiększyć prędkość, kiedy nie ma paliwa, prędkość niech pozostaje po prostu bez zmian).
​
Przetestuj swoje rozwiązanie i napisz testy, w których:
- zwiększysz prędkość pociągu o 5 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 20 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 8 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 10 km/h i wypisze jego opis
"""

class Train:
    def __init__(self):
        self.velocity = 10
        self.fuel_amount = 1000.0

    def accelerate(self, boost):
        if boost <= 0.75 * self.velocity:
            self.fuel_amount -= ((self.velocity + boost) - self.velocity) * (self.velocity / 100)

            if self.fuel_amount > 0:
                self.velocity += boost

        return self.velocity, self.fuel_amount

    def get_info(self):
        return f"Velocity: {self.velocity} km/h.\nAmount of fuel: {self.fuel_amount:.2f} litres."

    def __str__(self):
        return self.get_info()


train = Train()

train.accelerate(7.5)
train.accelerate(17.5 * 0.7)
train.accelerate(30 * 0.7)
train.accelerate(50 * 0.7)
train.accelerate(85 * 0.7)
train.accelerate(148 * 0.7)
train.accelerate(250 * 0.7)

info = train.get_info()
print(info)


def test_boost_5():
    train = Train()
    assert train.accelerate(5) == (15, 999.5)


def test_boost_7():
    train = Train()
    assert train.accelerate(7) == (17, 999.3)


def test_boost_20():
    train = Train()
    assert train.accelerate(20) == (10, 1000.0)


def test_boost_8():
    train = Train()
    assert train.accelerate(8) == (10, 1000.0)


def test_boost_10():
    train = Train()
    assert train.accelerate(10) == (10, 1000.0)


def test_fuel(): # sprawdzenie czy prędkość będzie taka sama jak skończy się paliwo
    train = Train()
    train.accelerate(7.5)
    train.accelerate(17.5 * 0.7)
    train.accelerate(30 * 0.7)
    train.accelerate(50 * 0.7)
    train.accelerate(85 * 0.7)
    train.accelerate(148 * 0.7)
    assert train.accelerate(250 * 0.7) == (423.85, 336.1084999999999)
    assert train.accelerate(100) == (423.85, -87.74150000000014)
