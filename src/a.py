class A:
    def __init__(self):
        self.x = 12  # normalna zmienna/pole (publiczna)

        self.__y = 'tego nie da sie odczytac majac referencje do instancji A'  # zmienna prywatna

    def get_y(self):  # pubczlina metoda
        return self.__y  # sposob na ekspozycje zmiennej prywatnej

    def __double_x(self):  # prywatna metoda (nie mozna jej wykonac majac referencje do instancji klasy A)
        self.x *= 2


a = A()
a.x = 18
print(a.x)

# a.__y = 99
try:
    print(a.__y)
except AttributeError:
    pass

print(a.get_y())

a.__double_x()
