class A:
    # "template"
    def __init__(self, name):
        self.name = name

    def salut(self):
        print(f'Hello {self.name}!')


# B jest A ... (orac/lub ma coś zmienione)
class B(A):
    """
    Ma mieć wszystko to co A + funkcję change_name(new_name: str).
    "B"
    """

    def change_name(self, new_name: str):
        self.name = new_name

    def salut(self):
        #super().salut()
        print(f'Greetings to {self.name}!')


def name_in_caps(instancja: A) -> str:
    return str(instancja.name).upper()


a = A('kadabra')
print(a.name)

b = A('abra')
print(b.name)
b.salut()

xx = B('xiao')
xx.salut()
xx.change_name('liaoning')
xx.salut()

print(name_in_caps(a))
print(name_in_caps(xx))
