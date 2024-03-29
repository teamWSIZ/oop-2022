import unittest

from src.z_0a_hydraulics.hydraulic_catalog import *
from src.z_0a_hydraulics.thread_definitions import *


class HydraulicTests(unittest.TestCase):

    def test_can_create_empty_adapter(self):
        adapter = Adapter_38Outer_14Innner()
        assert adapter.get_number_of_threads() == 2

    def test_can_link_adapter_to_14Outer_on_2nd_link(self):
        adapter = Adapter_38Outer_14Innner()
        element = WaterTap(Thread(size=Thread_1_4(), type=OuterThread()))
        adapter.connect_thread(element, thread_number=1, other_thread_number=0)
        assert adapter.get_connected_element_at(1) == element
        assert element.get_connected_element_at(0) == adapter

    def test_can_link_adapter_to_38Inner_on_1st_link(self):
        adapter = Adapter_38Outer_14Innner()
        element = WaterTap(Thread(size=Thread_3_8(), type=InnerThread()))
        adapter.connect_thread(element, thread_number=0, other_thread_number=0)

    def test_cant_link_adapter_to_38Outer_on_1st_link(self):
        adapter = Adapter_38Outer_14Innner()
        element = WaterTap(Thread(size=Thread_3_8(), type=OuterThread()))
        with self.assertRaises(IncompatibleThreadsError):
            adapter.connect_thread(element, thread_number=0, other_thread_number=0)

    def test_can_create_source(self):
        source = WaterSource(Thread(Thread_1_2(), OuterThread()))
        assert source.get_number_of_threads() == 1

    def test_can_connect_source_to_tap(self):
        source = WaterSource(Thread(Thread_1_2(), OuterThread()))
        tap = WaterTap(Thread(Thread_1_2(), InnerThread()))
        assert tap.get_number_of_threads() == 1
        source.connect_thread(tap, 0, 0)
        assert tap.get_connected_element_at(0) == source

    def test_can_disconnect_source_to_tap(self):
        source = WaterSource(Thread(Thread_1_2(), OuterThread()))
        tap = WaterTap(Thread(Thread_1_2(), InnerThread()))
        source.connect_thread(tap, 0, 0)

        source.disconnect(0)
        assert source.get_connected_element_at(0) is None

    def test_disconnecting_from_nonexistent_thread_raises(self):
        source = WaterSource(Thread(Thread_1_2(), OuterThread()))
        with self.assertRaises(HydraulicError):
            source.disconnect(10)
        with self.assertRaises(HydraulicError):
            source.disconnect(-1)

    def test_disconnecting_from_negative_thread_raises(self):
        source = WaterSource(Thread(Thread_1_2(), OuterThread()))
        tap = WaterTap(Thread(Thread_1_2(), InnerThread()))
        source.connect_thread(tap, 0, 0)

        with self.assertRaises(HydraulicError):
            source.disconnect(-1)

    def test_disconnecting_from_nonconnected_thread_raises(self):
        source = WaterSource(Thread(Thread_1_2(), OuterThread()))
        with self.assertRaises(HydraulicError):
            source.disconnect(0)

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

    def test_cannot_take_element_from_too_high_position(self):
        source = WaterSource(Thread(Thread_1_2(), OuterThread()))
        assert source.get_number_of_threads() == 1
        with self.assertRaises(HydraulicError):
            source.get_connected_element_at(1)  # only (0) would work

    def test_can_disconnect_elements(self):
        element1 = WaterSource(Thread(Thread_1_2(), OuterThread()))
        element2 = WaterSource(Thread(Thread_1_2(), InnerThread()))

        element1.connect_thread(element2, thread_number=0, other_thread_number=0)

        element1.disconnect(0)

        assert element1.get_connected_element_at(0) is None
        assert element2.get_connected_element_at(0) is None

    def test_can_disconnect_elements_in_case_of_multiple_threads(self):
        element1 = Connector([Thread(Thread_1_2(), OuterThread()), Thread(Thread_1_2(), OuterThread())])
        element2 = Connector([Thread(Thread_1_2(), InnerThread()), Thread(Thread_1_2(), InnerThread())])

        element1.connect_thread(element2, thread_number=0, other_thread_number=0)
        element1.connect_thread(element2, thread_number=1, other_thread_number=1)

        element1.disconnect(0)

        assert element1.get_connected_element_at(0) is None
        assert element2.get_connected_element_at(0) is None
        assert element1.get_connected_element_at(1) is element2
        assert element2.get_connected_element_at(1) is element1

    def test_disconnecting_from_none_raises(self):
        element1 = Connector([Thread(Thread_1_2(), OuterThread()), Thread(Thread_1_2(), OuterThread())])
        element2 = Connector([Thread(Thread_1_2(), InnerThread()), Thread(Thread_1_2(), InnerThread())])

        element1.connect_thread(element2, thread_number=0, other_thread_number=0)

        with self.assertRaises(HydraulicError):
            element1.disconnect(1)

    def test_disconnecting_twice_raises(self):
        element1 = Connector([Thread(Thread_1_2(), OuterThread()), Thread(Thread_1_2(), OuterThread())])
        element2 = Connector([Thread(Thread_1_2(), InnerThread()), Thread(Thread_1_2(), InnerThread())])

        element1.connect_thread(element2, thread_number=0, other_thread_number=0)
        element1.disconnect(0)

        with self.assertRaises(HydraulicError):
            element1.disconnect(0)

    def test_disconnecd_threads_are_reconnect_capable(self):
        element1 = Connector([Thread(Thread_1_2(), OuterThread()), Thread(Thread_1_2(), OuterThread())])
        element2 = Connector([Thread(Thread_1_2(), InnerThread()), Thread(Thread_1_2(), InnerThread())])

        element1.connect_thread(element2, thread_number=0, other_thread_number=0)
        element1.disconnect(0)

        element1.connect_thread(element2, thread_number=0, other_thread_number=0)

        assert element1.get_connected_element_at(0) is element2
        assert element2.get_connected_element_at(0) is element1


if __name__ == '__main__':
    unittest.main()
