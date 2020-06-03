"""
Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody` (z początkową wartością 0).

Niech ta klasa ma metody `dolej` i `odlej`. Obie metody niech przyjmują argument `ile` i niech odpowiednio
dodają lub odejmują tę liczbę do atrybutu `ilosc_wody`. Niech nie da się odlać więcej wody, niż jest w zbiorniku.

Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis `zbiornik z (ileś tam) litrami wody`.

Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`. Metoda dolej oprócz argumentu
`ile` powinna też przyjmować argument `temperatura` oznaczający temperaturę dolewanej wody. Dolanie wody do zbiornika
powinno powodować zmianę temperatury wody w zbiorniku (zgodnie ze zwykłymi prawami fizyki).
"""

# 4. Przerobic klase zbornik aby miwoda miała temperaturę.
# 5. przerobic metode "dolej" aby dolewana woda miała też temperaturę
# 6. dolewanie nowej wody do zbiornika zmienia temperaturę tej w zbiorniku.


import pytest


class Tank:
    def __init__(self, water_amount: int, tank_heat: int):
        self.water_amount = water_amount
        self.tank_heat = tank_heat

    def fill(self, how_much: int, heat: int):
        if self.tank_heat > heat:
            # zbiornik cieplejszy
            self.tank_heat = (self.water_amount * self.tank_heat + how_much * heat) / (how_much + self.water_amount)
        else:
            # dodana cieplejsza
            self.tank_heat = (how_much * heat + self.water_amount * self.tank_heat) / (how_much + self.water_amount)

        self.water_amount += how_much

        return self.water_amount, self.tank_heat

    def pour_off(self, how_much: int):
        if how_much > self.water_amount:
            raise ValueError("There is not enought water to pour off.")
        self.water_amount -= how_much
        return self.water_amount

    def info(self):
        return f"Tank water amount: {self.water_amount} litres.\nWater temperature is about {self.tank_heat:.1f} C"

    def __str__(self):
        return self.info()


water_tank = Tank(100, 50)
water_tank.fill(50, 30)
water_tank.pour_off(50)

print(water_tank.info())


def test_add_hotter_water():
    water_tank = Tank(100, 20)
    assert water_tank.fill(10, 50) == (110, 22.727272727272727)


def test_add_colder_water():
    water_tank = Tank(100, 50)
    assert water_tank.fill(50, 30) == (150, 43.333333333333336)


def test_pour_off():
    water_tank = Tank(100, 50)
    assert water_tank.pour_off(70) == 30


def test_cant_pour_off():
    water_tank = Tank(100, 50)
    with pytest.raises(ValueError):
        water_tank.pour_off(150)
