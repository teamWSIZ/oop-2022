import unittest

from src.t0.sec_system import SecurityGroup


class TestSecGroup(unittest.TestCase):

    def setUp(self) -> None:
        self.sg = SecurityGroup(1)

    def test_is_empty(self):
        for k in range(100):
            self.assertFalse(self.sg.has_key(k))
        for r in range(100):
            self.assertFalse(self.sg.has_resource(r))

    def test_can_assign_and_remove_key(self):
        self.sg.add_key(1)
        self.assertTrue(self.sg.has_key(1))
        self.sg.remove_key(1)
        self.assertFalse(self.sg.has_key(1))

    def test_can_assign_and_remove_resource(self):
        self.sg.add_resource(1)
        self.assertTrue(self.sg.has_resource(1))
        self.sg.remove_resource(1)
        self.assertFalse(self.sg.has_resource(1))

    def test_double_assign_changes_nothing(self):
        self.sg.add_key(1)
        self.sg.add_key(1)
        self.assertTrue(self.sg.has_key(1))
        self.sg.remove_key(1)
        self.assertFalse(self.sg.has_key(1))

    def test_can_hold_two_keys(self):
        self.sg.add_key(1)
        self.sg.add_key(2)
        self.assertTrue(self.sg.has_key(1))
        self.assertTrue(self.sg.has_key(2))
        self.sg.remove_key(1)
        self.assertFalse(self.sg.has_key(1))
        self.assertTrue(self.sg.has_key(2))

    def test_remove_absent_changes_nothing(self):
        self.sg.add_key(1)
        self.assertTrue(self.sg.has_key(1))
        self.sg.remove_key(2)
        self.assertTrue(self.sg.has_key(1))
        self.assertFalse(self.sg.has_key(2))
