class A:
    def __init__(self):
        self.x = 12


class B:
    def __init__(self):
        self.x = 12


a = A()
b = A()

print(type(a) == type(b))
