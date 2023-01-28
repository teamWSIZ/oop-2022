class A:
    def __init__(self):
        self._hidden = 1  # "protected variable"


class B(A):
    def __init__(self):
        super().__init__()

    def foo(self):
        print(self._hidden, id(self._hidden))


b = B()
b.foo()
print(id(b._hidden))