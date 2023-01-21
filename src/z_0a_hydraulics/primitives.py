# -- interfaces
import json


class HydraulicError(RuntimeError):
    pass


class IncompatibleThreadsError(HydraulicError):
    pass


class IElement:
    def __init__(self, threads: list['Thread']):
        self.__number_of_threads = len(threads)

        # references to other elements connected to this one
        self.__connected_elements: list['IElement'] = [None] * self.__number_of_threads

        # types of threads which this element possesses; populated for child types
        self.__threads: list['Thread'] = threads

    def connect_thread(self, other: 'IElement', thread_number: int, other_thread_number: int):
        """
        :param other: The element that will be connected to self
        :param thread_number: Number of thread on _self_ on which the connection is made
        :param other_thread_number: Number of thread on _other_ on which the connection is made
        :return:
        """
        self.__validate_thread_compatibility(self.__threads[thread_number], other.__threads[other_thread_number])

        self.__connected_elements[thread_number] = other

    def get_number_of_threads(self):
        # getter
        return self.__number_of_threads

    def __validate_thread_compatibility(self, thread1: 'Thread', thread2: 'Thread'):
        """
        Whole logic on which thread can be connected to which
        :param thread1:
        :param thread2:
        :raises IncompatibleThreadsError if threads are not compatible and cannot be connected
        :return:
        """
        # on PEP 8: E721 complaint:
        # https://stackoverflow.com/questions/52395064/e721-do-not-compare-types-use-isinstance-error
        if type(thread1.size) != type(thread2.size):
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

    def to_json(self):
        return 'thread size'


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

    def to_json(self):
        return 'thread type'


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

    def to_json(self):
        return self.__dict__


# ----------------- primitives


class Connector(IElement):

    def __init__(self, threads: list[Thread]):
        """
        Allows for a connection of `number_of_threads` different elements.
        :param threads: types of threads on each of the leg of the connector
        """
        super().__init__(threads)


class WaterSource(IElement):
    def __init__(self, thread: Thread):
        super().__init__([thread])


class WaterTap(IElement):
    def __init__(self, thread: Thread):
        super().__init__([thread])


# ------ tests

class Adapter_38Outer_14Innner(Connector):

    def __init__(self):
        left_thread = Thread(Thread_3_8(), OuterThread())
        right_thread = Thread(Thread_1_4(), InnerThread())
        super().__init__([left_thread, right_thread])


import unittest


class HydraulicTests(unittest.TestCase):

    def test_can_create_empty_adapter(self):
        adapter = Adapter_38Outer_14Innner()
        assert adapter.get_number_of_threads() == 2

    def test_can_link_adapter_to_14Outer_on_2nd_link(self):
        adapter = Adapter_38Outer_14Innner()
        element = WaterTap(Thread(size=Thread_1_4(), type=OuterThread()))
        adapter.connect_thread(element, 1, 0)

    def test_can_link_adapter_to_38Inner_on_1st_link(self):
        adapter = Adapter_38Outer_14Innner()
        element = WaterTap(Thread(size=Thread_3_8(), type=InnerThread()))
        adapter.connect_thread(element, thread_number=0, other_thread_number=0)

    def test_cant_link_adapter_to_38Outer_on_1st_link(self):
        adapter = Adapter_38Outer_14Innner()
        element = WaterTap(Thread(size=Thread_3_8(), type=OuterThread()))
        with self.assertRaises(IncompatibleThreadsError):
            adapter.connect_thread(element, thread_number=0, other_thread_number=0)



    # def test_can_create_source(self):
    #     source = WaterSource(Thread(Thread_1_2(), OuterThread()))
    #     print(source.__dict__)
    #     print(json.dumps(source.__dict__))

    def test_can_create_source(self):
        source = WaterSource(Thread(Thread_1_2(), OuterThread()))
        assert source.get_number_of_threads() == 1

    def test_can_connect_source_to_tap(self):
        source = WaterSource(Thread(Thread_1_2(), OuterThread()))
        tap = WaterTap(Thread(Thread_1_2(), InnerThread()))
        assert tap.get_number_of_threads() == 1
        source.connect_thread(tap, 0, 0)

    def test_can_connect_via_adapter_1_4_to_3_8(self):
        source = WaterSource(Thread(Thread_3_8(), InnerThread()))
        adapter = Adapter_38Outer_14Innner()
        tap = WaterTap(Thread(Thread_1_4(), OuterThread()))

        source.connect_thread(adapter, 0, 0)
        adapter.connect_thread(tap, 1, 0)

    def test_cant_connect_to_same_thread_twice(self):
        adapter = Adapter_38Outer_14Innner()
        element = WaterTap(Thread(size=Thread_1_4(), type=OuterThread()))
        adapter.connect_thread(element, 1, 0)
        with self.assertRaises(HydraulicError):
            adapter.connect_thread(element, 1, 0)
