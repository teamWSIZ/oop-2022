import unittest

from src.t0.errors import SecurityUnauthorized, SecurityBadRequest
from src.t0.model import SecuredResource
from src.t0.sec_system import SecurityManager, LockManager


class TestSecGroup(unittest.TestCase):

    def setUp(self) -> None:
        self.mgr = SecurityManager()
        self.group_id = self.mgr.create_group()

        self.mgr.add_key_to_group(executor_id=0, key_id=1, group_id=self.group_id)
        self.mgr.add_resource_to_group(executor_id=0, resource_id=1, group_id=self.group_id)

        self.lock_mgr = LockManager(self.mgr)
        res1 = SecuredResource(1, 'bezpieczniki', is_open=False)
        res2 = SecuredResource(1, 'zawór główny gazu', is_open=False)
        self.lock_mgr.add_resource(res1)
        self.lock_mgr.add_resource(res2)

    def test_user1_opens_res1(self):
        self.lock_mgr.unlock(key_id=1, resource_id=1)

    def test_admin_cannot_open_res1(self):
        with self.assertRaises(SecurityUnauthorized):
            self.lock_mgr.unlock(key_id=0, resource_id=1)

    def test_user1_opens_locks_opens_res1(self):
        self.lock_mgr.unlock(key_id=1, resource_id=1)
        self.lock_mgr.lock(key_id=1, resource_id=1)
        self.lock_mgr.unlock(key_id=1, resource_id=1)

    def test_user2_opens_res1_when_authorized(self):
        with self.assertRaises(SecurityUnauthorized):
            self.lock_mgr.unlock(key_id=2, resource_id=1)
        self.mgr.add_key_to_group(executor_id=0, key_id=2, group_id=self.group_id)

        self.lock_mgr.unlock(key_id=2, resource_id=1)  # no throw

    def test_admin_can_unauthorize(self):
        self.mgr.remove_key_to_group(executor_id=0, key_id=1, group_id=self.group_id)
        with self.assertRaises(SecurityUnauthorized):
            self.lock_mgr.unlock(key_id=1, resource_id=1)

    def test_double_unlock_raises_securitybadrequest(self):
        self.lock_mgr.unlock(key_id=1, resource_id=1)
        with self.assertRaises(SecurityBadRequest):
            self.lock_mgr.unlock(key_id=1, resource_id=1)

    def test_double_lock_raises_securitybadrequest(self):
        self.lock_mgr.unlock(key_id=1, resource_id=1)
        self.lock_mgr.lock(key_id=1, resource_id=1)
        with self.assertRaises(SecurityBadRequest):
            self.lock_mgr.lock(key_id=1, resource_id=1)
