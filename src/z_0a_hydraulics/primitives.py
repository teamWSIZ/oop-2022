# -- interfaces


class HydraulicError(RuntimeError):
    pass


class IncompatibleThreadsError(HydraulicError):
    pass


class IElement:
    def __init__(self, number_of_threads: int):
        self.number_of_threads = number_of_threads

        # references to other elements connected to this one
        self.connected_elements: list['IElement'] = [None] * number_of_threads

        # types of threads which this element possesses; populated for child types
        self.threads: list['Thread'] = [None] * number_of_threads

    def connect_thread(self, other: 'IElement', thread_number: int, other_thread_number: int):
        """
        :param other: The element that will be connected to self
        :param thread_number: Number of thread on _self_ on which the connection is made
        :param other_thread_number: Number of thread on _other_ on which the connection is made
        :return:
        """
        self.__validate_thread_compatibility(self.threads[thread_number], other.threads[other_thread_number])

        self.connected_elements[thread_number] = other

    def __validate_thread_compatibility(self, thread1: 'Thread', thread2: 'Thread'):
        """
        Whole logic on which thread can be connected to which
        :param thread1:
        :param thread2:
        :raises IncompatibleThreadsError if threads are not compatible and cannot be connected
        :return:
        """
        if type(thread1.size) != type(thread2.size):  # todo: WTF?? repair using isinstance ??
            raise IncompatibleThreadsError('Sizes of both threads are not same')

        # only positive connections listed; else: error
        if isinstance(thread1.type, InnerThread) and isinstance(thread2.type, OuterThread):
            return
        if isinstance(thread1.type, OuterThread) and isinstance(thread2.type, InnerThread):
            return

        # no valid case of junction found --> raise error
        raise IncompatibleThreadsError('Types of threads on both sides are not compatible')



class IThreadSize:
    verbal: str


class Thread_3_8(IThreadSize):
    def __init__(self):
        self.verbal = '3/8'


class Thread_1_2(IThreadSize):
    def __init__(self):
        self.verbal = '1/2'


class Thread_1_4(IThreadSize):
    def __init__(self):
        self.verbal = '1/4'


class IThreadType:
    verbal: str


class InnerThread(IThreadType):
    def __init__(self):
        self.verbal = 'inner thread'


class OuterThread(IThreadType):
    def __init__(self):
        self.verbal = 'outer thread'


class Thread:

    def __init__(self, size: IThreadSize, type: IThreadType):
        self.size = size  # 3/8, 1/2,
        self.type = type  # inner/outer


# ----------------- primitives


class Connector(IElement):

    def __init__(self, threads: list[Thread]):
        """
        Allows for a connection of `number_of_threads` different elements.
        :param threads: types of threads on each of the leg of the connector
        :param number_of_threads: total number of legs
        """
        self.number_of_threads = len(threads)
        super().__init__(self.number_of_threads)

        self.threads = threads


class WaterSource(IElement):
    def __init__(self, thread: Thread):
        super().__init__(1)
        self.threads[0] = thread


class WaterTap(IElement):
    def __init__(self, thread: Thread):
        super().__init__(1)
        self.threads[0] = thread


# ------ tests

class Adapter_3_8_to_1_4(Connector):

    def __init__(self):
        left_thread = Thread(Thread_3_8(), OuterThread())
        right_thread = Thread(Thread_1_4(), InnerThread())
        super().__init__([left_thread, right_thread])


import unittest


class HydraulicTests(unittest.TestCase):

    def test_can_connect_source_to_tap(self):
        source = WaterSource(Thread(Thread_1_2(), OuterThread()))
        tap = WaterTap(Thread(Thread_1_2(), InnerThread()))
        source.connect_thread(tap, 0, 0)

    def test_can_connect_via_adapter_1_4_to_3_8(self):
        source = WaterSource(Thread(Thread_3_8(), InnerThread()))
        adapter = Adapter_3_8_to_1_4()
        tap = WaterTap(Thread(Thread_1_4(), OuterThread()))

        source.connect_thread(adapter, 0, 0)
        adapter.connect_thread(tap, 1, 0)
