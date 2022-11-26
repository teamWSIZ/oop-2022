

class MyError(RuntimeError):
    pass

def goo():
    print('starting goo')
    try:
        foo()
    except RuntimeError as e:
        print('nie udalo sie:', e)

    print('finishing goo')

def foo():
    print('in foo')
    raise MyError('meh... not again')
    print('finishing foo')

if __name__ == '__main__':
    goo()
