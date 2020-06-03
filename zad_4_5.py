"""Napisz klasę `Zolw` z metodami `idz` i `obroc_sie`. Żółw ma jakieś położenie (wyrażone dwiema współrzędnymi) i jakieś
ustawienie, czyli kurs (wyznaczony pojedyncza liczba).

Początkowe położenie podajemy konstruktorowi klasy, początkowy kurs to zawsze 0.

Metoda `obroc_sie ` powoduje obrót żółwia, czyli zmianę jego kursu.

Metoda `idz` powoduje przejście żółwia o określoną odległość.

Z klasy będzie się korzystać tak:

```python
z = Zolw(100, 100)
z.idz(50)

print(z) # ma sie wypisac: x=100, y=50

z.obroc_sie(90)
z.idz(50)

print(z) # ma sie wypisac: x=150, y=50
```
"""
import pytest


class Turtle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.degree = 0

    def turn(self, add_degree: int) -> int:
        """
        Turtle turn amount
        :param add_degree: must be number of 0, 90, 180, 270 or 360
        :return: turn degree
        """
        if add_degree != 0 and add_degree != 90 and add_degree != 180 and add_degree != 270 and add_degree != 360:
            raise ValueError("Incorect degree value")
        self.degree += add_degree
        if self.degree > 360:
            self.degree -= 360
        return self.degree

    def go(self, distance: int):
        """
        Distance for turtle to cover. Dependent on turn degree.
        :param distance:
        :return:
        """
        if self.degree == 0:
            self.y += distance
        elif self.degree == 90:
            self.x += distance
        elif self.degree == 180:
            self.y -= distance
        elif self.degree == 270:
            self.x -= distance
        elif self.degree == 360:
            self.y += distance
        return self.x, self.y

    def get_info(self):
        if self.degree == 0 or self.degree == 360:
            return f"Turtle positrion: x = {self.x}, y = {self.y}.\nDirection: up"
        elif self.degree == 90:
            return f"Turtle positrion: x = {self.x}, y = {self.y}.\nDirection: right"
        elif self.degree == 180:
            return f"Turtle positrion: x = {self.x}, y = {self.y}.\nDirection: down"
        elif self.degree == 270:
            return f"Turtle positrion: x = {self.x}, y = {self.y}.\nDirection: left"

    def __str__(self):
        return self.get_info()

    def position(self):
        return self.x, self.y


turtle = Turtle(0, 0)
turtle.turn(0)
turtle.go(2)
turtle.turn(180)
turtle.go(15)
turtle.turn(180)
turtle.go(15)
turtle.turn(90)
turtle.go(1)
turtle.turn(180)
turtle.go(10)


print(turtle.get_info())


def test_invalid_turn_value():
    turtle = Turtle(0, 0)
    with pytest.raises(ValueError):
        turtle.turn(15)

def test_go_right():
    turtle = Turtle(0, 0)
    turtle.turn(90)
    assert turtle.go(5) == (5, 0)

def test_go_down():
    turtle = Turtle(0, 0)
    turtle.turn(180)
    assert turtle.go(5) == (0, -5)

def test_multiple_turns():
    turtle = Turtle(0, 0)
    turtle.turn(90)
    turtle.turn(270)
    turtle.turn(180)
    assert turtle.go(10) == (0, -10)
