import unittest

from src.z7_parking.places import Parking
from src.z7_parking.vehicles import Vehicle


class ParkingTest(unittest.TestCase):

    def test_parking_vehicle_enters_leaves(self):
        v = Vehicle()
        p = Parking()

        p.enter(v)
        p.leave(v)

    def test_parking_vehicle_entered_is_at_parking(self):
        v = Vehicle()
        p = Parking()

        p.enter(v)

        self.assertEqual(v.place, p)
        self.assertTrue(True)
