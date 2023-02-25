"""
Ilustracja działania Method Resolution Order (MRO)
"""


class B1:

    def foo(self):
        print('one')


class B2:

    def foo(self):
        print('two')


class C(B1, B2):

    def goo(self):
        print('works')


if __name__ == '__main__':
    c = C()
    c.foo()
    print(C.__mro__)
