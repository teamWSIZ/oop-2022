"""
Klasy dziedziczące nie mają dostępu do zmiennych prywatnych klasy bazowej.
"""

class A:
    def __init__(self):
        self.__x = 10


class B(A):
    def __init__(self):
        super().__init__()

    def change_x(self):
        print(self.__x)  # error -- no such attribute -- nie mamy dostepu do zmiennych prywatnych
        self.__x = 20


b = B()
b.change_x()
