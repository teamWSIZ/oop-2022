from src.z_0a_hydraulics.base_objects import *
from src.z_0a_hydraulics.thread_definitions import *


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


class Adapter_38Outer_14Innner(Connector):

    def __init__(self):
        left_thread = Thread(Thread_3_8(), OuterThread())
        right_thread = Thread(Thread_1_4(), InnerThread())
        super().__init__([left_thread, right_thread])
