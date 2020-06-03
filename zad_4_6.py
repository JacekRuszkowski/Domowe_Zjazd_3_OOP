"""
Stwórz klasę `PlanszaXO` - jej obiekty mają reprezentować stan planszy do gry w kółko i krzyżyk.

Ma ona mieć metody:
`dodaj_element(x: int, y: int, rodzaj_elementu)`
W argumencie `rodzaj_elementu` będzie napis `"x"` lub `"o"`. Jeśli ruch jest nieprawidłowy, metoda powinna
zwracać fałsz.

`stan_gry()`
Ta metoda ma zwracać liczbę oznaczającą stan gry (gra trwa, gra zakończona sukcesem krzyżyków, gra zakończona
sukcesem kółek).

`czyj_ruch()`
Ta metoda ma powiedzieć, czyj ruch ma być teraz (kółek czy krzyżyków).

Wyświetlenie obiektu tej klasy ma wypisać planszę.

Użyj tej klasy do zrobienia gry w kółko i krzyżyk.
"""


#         self.plansza = {"1": (3, 1), "2": (3, 2), "3": (3, 3),
#                         "4": (2, 1), "5": (2, 2), "6": (2, 3),
#                         "7": (1, 1), "8": (2, 1), "9": (3, 1)}
#

class PlanszaXO:
    def __init__(self):
        self.plansza = {"1": " ", "2": " ", "3": " ",
                        "4": " ", "5": " ", "6": " ",
                        "7": " ", "8": " ", "9": " "}

    def wyswietl(self):

        print(f"3 {self.plansza['1']}|{self.plansza['2']}|{self.plansza['3']}")
        # print(f"-+-+-")
        print(f"2 {self.plansza['4']}|{self.plansza['5']}|{self.plansza['6']}")
        # print(f"-+-+-")
        print(f"1 {self.plansza['7']}|{self.plansza['8']}|{self.plansza['9']}")
        print("  1 2 3")
        print()

    def ruch(self, element: str):
        if element == "x":
            print("Ruch krzyżyka.")
        elif element == "o":
            print("Ruch kółka.")
        x = int(input("Podaj pozycje na osi x: "))
        y = int(input("Podaj pozycję na osi y: "))
        # for keys, values in self.plansza.items():  # sprawdzenie czy pole jest puste
        #     if self.plansza[keys] != " ":
        #         raise ValueError("To miejsce jest juz zajęte!")
        #     else:
        if element == 'x':  # zaznaczenie elementu "x"
            if x == 1 and y == 1 and self.plansza["7"] == " ":
                self.plansza["7"] = 'x'
            elif x == 1 and y == 2 and self.plansza["4"] == " ":
                self.plansza["4"] = 'x'
            elif x == 1 and y == 3 and self.plansza["1"] == " ":
                self.plansza["1"] = 'x'
            elif x == 2 and y == 1 and self.plansza["8"] == " ":
                self.plansza["8"] = 'x'
            elif x == 2 and y == 2 and self.plansza["5"] == " ":
                self.plansza["5"] = 'x'
            elif x == 2 and y == 3 and self.plansza["2"] == " ":
                self.plansza["2"] = 'x'
            elif x == 3 and y == 1 and self.plansza["9"] == " ":
                self.plansza["9"] = 'x'
            elif x == 3 and y == 2 and self.plansza["6"] == " ":
                self.plansza["6"] = 'x'
            elif x == 3 and y == 3 and self.plansza["3"] == " ":
                self.plansza["3"] = 'x'

        if element == 'o':  # zaznaczenie elementu "o"
            if x == 1 and y == 1 and self.plansza["7"] == " ":
                self.plansza["7"] = 'o'
            elif x == 1 and y == 2 and self.plansza["4"] == " ":
                self.plansza["4"] = 'o'
            elif x == 1 and y == 3 and self.plansza["1"] == " ":
                self.plansza["1"] = 'o'
            elif x == 2 and y == 1 and self.plansza["8"] == " ":
                self.plansza["8"] = 'o'
            elif x == 2 and y == 2 and self.plansza["5"] == " ":
                self.plansza["5"] = 'o'
            elif x == 2 and y == 3 and self.plansza["2"] == " ":
                self.plansza["2"] = 'o'
            elif x == 3 and y == 1 and self.plansza["9"] == " ":
                self.plansza["9"] = 'o'
            elif x == 3 and y == 2 and self.plansza["6"] == " ":
                self.plansza["6"] = 'o'
            elif x == 3 and y == 3 and self.plansza["3"] == " ":
                self.plansza["3"] = 'o'

    def stan_gry(self):
        if self.plansza["7"] == self.plansza["5"] == self.plansza["3"] == "x" != " ":  # 1 przekątna
            print("Koniec gry. Wygrał krzyżyk.")
        elif self.plansza["1"] == self.plansza["5"] == self.plansza["9"] == "x" != " ": # 2 przekątna
            print("Koniec gry. Wygrał krzyżyk.")
        elif self.plansza["7"] == self.plansza["8"] == self.plansza["9"] == "x" != " ": # dół poziomo
            print("Koniec gry. Wygrał krzyżyk.")
        elif self.plansza["4"] == self.plansza["5"] == self.plansza["6"] == "x" != " ": # środek poziomo
            print("Koniec gry. Wygrał krzyżyk.")
        elif self.plansza["1"] == self.plansza["2"] == self.plansza["3"] == "x" != " ": # góra poziomo
            print("Koniec gry. Wygrał krzyżyk.")
        elif self.plansza["1"] == self.plansza["4"] == self.plansza["7"] == "x" != " ": # lewy pion
            print("Koniec gry. Wygrał krzyżyk.")
        elif self.plansza["2"] == self.plansza["5"] == self.plansza["8"] == "x" != " ": # środkowy_pion
            print("Koniec gry. Wygrał krzyżyk.")
        elif self.plansza["3"] == self.plansza["6"] == self.plansza["9"] == "x" != " ": # prawy_pion
            print("Koniec gry. Wygrał krzyżyk.")

        elif self.plansza["1"] == self.plansza["5"] == self.plansza["9"] == "o" != " ": # 2 przekątna
            print("Koniec gry. Wygrał 'o'")
        elif self.plansza["7"] == self.plansza["8"] == self.plansza["9"] == "o" != " ": # dół poziomo
            print("Koniec gry. Wygrał 'o'")
        elif self.plansza["4"] == self.plansza["5"] == self.plansza["6"] == "o" != " ": # środek poziomo
            print("Koniec gry. Wygrał 'o'")
        elif self.plansza["1"] == self.plansza["2"] == self.plansza["3"] == "o" != " ": # góra poziomo
            print("Koniec gry. Wygrał 'o'")
        elif self.plansza["1"] == self.plansza["4"] == self.plansza["7"] == "o" != " ": # lewy pion
            print("Koniec gry. Wygrał 'o'")
        elif self.plansza["2"] == self.plansza["5"] == self.plansza["8"] == "o" != " ": # środkowy_pion
            print("Koniec gry. Wygrał 'o'")
        elif self.plansza["3"] == self.plansza["6"] == self.plansza["9"] == "o" != " ": # prawy_pion
            print("Koniec gry. Wygrał 'o'")

        else:
            print("Gra w toku")





gra = PlanszaXO()
gra.wyswietl()
gra.ruch("x")
gra.wyswietl()
gra.ruch("o")
gra.wyswietl()
gra.ruch("x")
gra.wyswietl()
gra.stan_gry()
gra.ruch("o")
gra.wyswietl()
gra.stan_gry()
gra.ruch("x")
gra.wyswietl()
gra.stan_gry()
gra.ruch("o")
gra.wyswietl()
gra.stan_gry()
gra.ruch("x")
gra.wyswietl()
gra.stan_gry()
gra.ruch("o")
gra.wyswietl()
gra.stan_gry()
gra.ruch("x")
gra.wyswietl()
gra.stan_gry()
gra.ruch("o")
gra.wyswietl()
gra.stan_gry()



