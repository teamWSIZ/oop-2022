class HydraulicError(RuntimeError):
    pass


class IncompatibleThreadsError(HydraulicError):
    pass


if __name__ == '__main__':
    try:
        raise IncompatibleThreadsError('the right thread is too large')
    except HydraulicError as e:
        print('-->', str(e))
