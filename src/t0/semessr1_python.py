import unittest


def zad1(a):
    return chr((25 - (ord(a) - 97)) + 97)


def zad2(b):
    return int("".join(list(map(str, str(b)))[::-1]))


def zad3(c):
    return "".join([i.upper() if i.islower() else i.lower() for i in c])


class SecurityTests(unittest.TestCase):
    def test_zad1(self):
        assert zad1("a") == "z"
        assert zad1("b") == "y"
        assert zad1("c") == "x"
        assert zad1("d") == "w"
        assert zad1("e") == "v"
        assert zad1("f") == "u"

    def test_zad2(self):
        assert zad2(123) == 321
        assert zad2(1111) == 1111
        assert zad2(1234) == 4321
        assert zad2(123) == 321
        assert zad2(1111) == 1111
        assert zad2(1234) == 4321

    def test_zad3(self):
        assert zad3("aab") == "AAB"
        assert zad3("aaB") == "AAb"
        assert zad3("aAb") == "AaB"
        assert zad3("AAB") == "aab"
        assert zad3("aabe") == "AABE"
        assert zad3("a") == "A"


def zad7(d):
    s = d
    while True:
        if s <= 9:
            break
        else:
            s = sum([int(i) for i in str(s)])
    return s


def zad8(e):
    l = []
    for i in range(1, e // 2 + 1):
        if e % i == 0: l.append(i)
    l.append(e)
    return l


def zad9(f):
    b = 0
    l = len(f) + 1
    for e in range(0, l):
        for i in range(e, l):
            if sum(f[e:i]) > b:
                b = sum(f[e:i])
            print(f[e:i])

    print(b)


zad9([1, -2, 3, -4, 5, -4, 5, -2, 1])
