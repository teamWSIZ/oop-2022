

def foo():
    # raise ExceptionGroup('abra kadabra!', [IndexError('wrong index'), ZeroDivisionError("meh... don't do this")])
    raise ComplexError('gotcha!')



class ComplexError(IndexError, ZeroDivisionError):
    pass


if __name__ == '__main__':
    try:
        foo()
    # except IndexError as e:
    #     print(e)
    except ZeroDivisionError as e:
        print(e)
