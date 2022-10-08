from dataclasses import dataclass


@dataclass
class A:
    uid: int
    name: str


def is_valid(instance: A) -> bool:
    """
    Checks if the `instance` is fulfilling the requirements
    :param instance:
    :return: True if `instance` is OK
    """
    if (instance.uid == None or instance.uid < 0 or len(instance.name)==0):
        return False
    if (instance.name[0].isdigit()):
        return False
    return True


if __name__ == '__main__':
    # twrzymy "instancję" klasy
    a = A(10, 'abc')
    b = A(11, 'xxx')    #druga, niezależna instancja
    print(id(a))
    print(id(b))
    print(a)
    print(b)
    print(a.uid)
    print(f'instancja "a" jest valid? {is_valid(a)}')

