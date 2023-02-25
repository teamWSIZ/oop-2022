from src.z_0a_hydraulics.errors import IncompatibleThreadsError, HydraulicError
from src.z_0a_hydraulics.thread_definitions import InnerThread, OuterThread


class IElement:
    def __init__(self, threads: list['Thread']):
        self.__number_of_threads = len(threads)

        # references to other elements connected to this one
        self.__connected_elements: list['IElement'] = [None] * self.__number_of_threads

        # types of threads which this element possesses; populated for child types
        self.__threads: list['Thread'] = threads  # todo: "immutable"

    def connect_thread(self, other: 'IElement', thread_number: int, other_thread_number: int):
        """
        :param other: The element that will be connected to self
        :param thread_number: Number of thread on _self_ on which the connection is made
        :param other_thread_number: Number of thread on _other_ on which the connection is made
        :return:
        """
        self.__validate_thread_compatibility(self.__threads[thread_number], other.__threads[other_thread_number])

        if (self.__connected_elements[thread_number] is None) and \
                (other.__connected_elements[other_thread_number] is None):
            self.__connected_elements[thread_number] = other
            other.__connected_elements[other_thread_number] = self
        else:
            raise HydraulicError()

    def get_number_of_threads(self):
        # getter
        return self.__number_of_threads

    def get_connected_element_at(self, position: int):
        max_threads = self.get_number_of_threads()
        if position >= max_threads:
            raise HydraulicError(f'Asking for element at {position=} beyond the range of the number of threads'
                                 f' (={max_threads})')
        return self.__connected_elements[position]

    def disconnect(self, position: int):
        print(f'disconnecting at {position=}')
        max_position = self.get_number_of_threads() - 1
        if position > max_position or position < 0:
            raise HydraulicError('no no no -- diconnecting from nonexistent thread')

        if self.__connected_elements[position] is None:
            raise HydraulicError('no no no -- diconnecting from non-connected thread')

        other = self.__connected_elements[position]
        other_position = None
        # znaleźć pozycję na której jest `self` podłączony...
        for (pos, element) in enumerate(other.__connected_elements):
            if element == self:
                other_position = pos
                break
        else:
            raise HydraulicError(
                'consistency error: current element is nowhere to be found among connected elements of the other')

        # actual disconnect
        other.__connected_elements[other_position] = None
        self.__connected_elements[position] = None

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
