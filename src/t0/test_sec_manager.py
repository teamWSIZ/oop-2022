import unittest

from src.t0.errors import SecurityUnauthorized
from src.t0.sec_system import SecurityManager


class TestSecGroup(unittest.TestCase):

    def setUp(self) -> None:
        self.mgr = SecurityManager()
        self.group_id = self.mgr.create_group()
        self.mgr.add_key_to_group(0, key_id=1, group_id=self.group_id)
        self.mgr.add_resource_to_group(0, resource_id=1, group_id=self.group_id)

    def test_admin_opens_0(self):
        self.assertTrue(self.mgr.check_key_opens_resource(0, 0))

    def test_only_one_admin(self):
        for k in range(1, 100):
            self.assertFalse(self.mgr.check_key_opens_resource(k, 0))

    def test_key1_opens_res1(self):
        self.assertTrue(self.mgr.check_key_opens_resource(key_id=1, resource_id=1))

    def test_can_add_sec_group(self):
        # no exception
        self.mgr.create_group()

    def test_key1_does_not_open_res2(self):
        g2 = self.mgr.create_group()
        self.mgr.add_resource_to_group(0, resource_id=2, group_id=g2)
        self.assertFalse(self.mgr.check_key_opens_resource(key_id=1, resource_id=2))

    def test_key1_create_group_raises(self):
        with self.assertRaises(SecurityUnauthorized):
            self.mgr.create_group(executor_id=1)

    def test_key1_add_admin_raises(self):
        with self.assertRaises(SecurityUnauthorized):
            self.mgr.add_key_to_group(executor_id=1, key_id=1, group_id=0)

    def test_key0_can_create_admin(self):
        self.mgr.add_key_to_group(executor_id=0, key_id=1, group_id=0)
        self.assertTrue(self.mgr.is_admin(key_id=1))