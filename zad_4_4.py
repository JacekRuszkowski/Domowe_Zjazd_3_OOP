"""
Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody` (z początkową wartością 0).

Niech ta klasa ma metody `dolej` i `odlej`. Obie metody niech przyjmują argument `ile` i niech odpowiednio
dodają lub odejmują tę liczbę do atrybutu `ilosc_wody`. Niech nie da się odlać więcej wody, niż jest w zbiorniku.

Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis `zbiornik z (ileś tam) litrami wody`.

Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`. Metoda dolej oprócz argumentu
`ile` powinna też przyjmować argument `temperatura` oznaczający temperaturę dolewanej wody. Dolanie wody do zbiornika
powinno powodować zmianę temperatury wody w zbiorniku (zgodnie ze zwykłymi prawami fizyki).
"""

# 1. stworzyć klase Zbiornik z atrubutem - ile wody
# 2. stworzyć metody dolej i odlej z arumentami "ile". Moga dodawać i odejmować wode ze zbiornika. Nie można odjąć
#    więcej niż jest wody w zbiorniku.
# 3. Wypisać informację ile wody jest w zbiorniku (ile litrow).

import pytest


class Tank:
    def __init__(self, water_amount: float):
        self.water_amount = water_amount

    def fill(self, how_much: float):
        self.water_amount += how_much
        return self.water_amount

    def pour_off(self, how_much: float):
        if how_much > self.water_amount:
            raise ValueError("There is not enought water to pour off.")
        self.water_amount -= how_much
        return self.water_amount

    def info(self):
        return f"Tank water amount: {self.water_amount} litres."

    def __str__(self):
        return self.info()

water_tank = Tank(100)

water_tank.fill(50)
water_tank.fill(50)
water_tank.pour_off(20)
water_tank.pour_off(150)

print(water_tank.info())


def test_add_water():
    water_tank = Tank(100)
    water_tank.fill(10)
    assert water_tank.fill(50) == 160


def test_pour_off():
    water_tank = Tank(100)
    assert water_tank.pour_off(70) == 30

def test_cant_pour_off():
    water_tank = Tank(100)
    with pytest.raises(ValueError):
        water_tank.pour_off(150)


