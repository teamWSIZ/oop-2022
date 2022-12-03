import unittest

from src.z7_parking.errorz import *
from src.z7_parking.financial import MonetaryParkingError
from src.z7_parking.places import Parking, TollParking
from src.z7_parking.vehicles import Vehicle, PremiumCar


class ParkingTest(unittest.TestCase):

    def test_parking_vehicle_enters_leaves(self):
        v = Vehicle()
        p = Parking()

        p.enter(v)
        p.leave(v)

        assert p.get_max_capacity() == p.get_free_capacity()

    def test_parking_vehicle_entered_is_at_parking(self):
        v = Vehicle()
        p = Parking()
        before_capacity = p.get_free_capacity()

        p.enter(v)
        now_capacity = p.get_free_capacity()

        self.assertEqual(v.place, p)
        self.assertEqual(now_capacity, before_capacity - 1)

    def test_vehicle_can_move_between_places(self):
        v = Vehicle()
        p1 = Parking()
        p2 = Parking()

        p1.enter(v)
        p2.enter(v)

        self.assertEqual(v.place, p2)
        self.assertEqual(p1.get_free_capacity(), p1.get_max_capacity())

    def test_vehicle_cannot_reenter(self):
        v = Vehicle()
        p = Parking()
        p.enter(v)

        with self.assertRaises(ParkingSystemError):
            p.enter(v)

    def test_vehicle_cannot_enter_full_parking(self):
        v1 = Vehicle()
        v2 = Vehicle()
        p = Parking(max_capacity=1)
        p.enter(v1)

        with self.assertRaises(ParkingFullError):
            p.enter(v2)

    def test_nonbillable_cannot_access_parking(self):
        v1 = Vehicle()
        p = TollParking()

        with self.assertRaises(MonetaryParkingError):
            p.enter(v1)

    def test_billable_can_access_parking(self):
        v1 = PremiumCar()
        p = TollParking()

        p.enter(v1)

    def test_vehicle_is_correctly_billed(self):
        raise NotImplementedError()

    def test_parking_collects_monies(self):
        raise NotImplementedError()
