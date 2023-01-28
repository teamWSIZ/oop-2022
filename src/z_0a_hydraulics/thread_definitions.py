class IThreadSize:
    verbal: str

    def to_json(self):
        return 'thread size'


class IThreadType:
    verbal: str

    def to_json(self):
        return 'thread type'


# todo: disallow creating instances of Thread; must subclass it
class Thread:

    def __init__(self, size: IThreadSize, type: IThreadType):
        self.size = size  # 3/8, 1/2,
        self.type = type  # inner/outer


#(todo)  specific definitions of sizes

class Thread_3_8(IThreadSize):
    def __init__(self):
        self.verbal = '3/8'


class Thread_1_2(IThreadSize):
    def __init__(self):
        self.verbal = '1/2'


class Thread_1_4(IThreadSize):
    def __init__(self):
        self.verbal = '1/4'


#(todo)  specific definitions of sizes

class InnerThread(IThreadType):
    def __init__(self):
        self.verbal = 'inner thread'


class OuterThread(IThreadType):
    def __init__(self):
        self.verbal = 'outer thread'
