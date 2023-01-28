class HydraulicError(RuntimeError):
    pass


class IncompatibleThreadsError(HydraulicError):
    pass

#
# class A:
#     def __init__(self, x=12):
#         self.x = x
#
#
# a = A
# inst_a = a()
# print(type(inst_a))
# print(inst_a.x)

if __name__ == '__main__':
    try:
        raise IncompatibleThreadsError('the right thread is too large')
    except HydraulicError as e:
        print('-->', str(e))
