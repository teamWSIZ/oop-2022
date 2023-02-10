

if __name__ == '__main__':
    try:
        excs = [OSError('error 1'), SystemError('error 2')]
        raise ExceptionGroup('there were problems', excs)
    except* OSError as e:
        print('OS error present: ', e)  # this is executed
    except* SystemError as e:
        print('SystemError present: ', e) # this is executed too

