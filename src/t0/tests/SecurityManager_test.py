import random
import unittest

from sesja.models.securityGroup import SecurityGroup
from sesja.models.key import Key
from sesja.models.securityManager import SecurityManager
from sesja.errors.unauthorized import SecurityUnauthorized


class SecurityTests(unittest.TestCase):

    def test_can_add_key_to_group(self):
        group = SecurityGroup(3)
        key = Key(1, "MARY'S KEY")
        s_manager = SecurityManager()
        s_manager.create_group_example()
        s_manager.add_key_to_group(2, key.id, group.group_id)

    def test_executor_id_can_add(self):
        s_manager = SecurityManager()
        s_manager.add_key_to_group(2, 1, 0)
        assert s_manager.groups[0].keys == set([1])

    def test_can_not_remove_key(self):
        mgr = SecurityManager()
        mgr.add_key_to_group(0, 1, 0)
        self.assertRaises(SecurityUnauthorized, lambda: mgr.remove_key_from_group(2 * random.randint(1, 10 ** 3), 1, 0))
        # this value must be even (2 * random.randint(1, 10 ** 3) -> 2x
    def test_example_group(self):
        s_manager = SecurityManager()
        s_manager.create_group_example()
        print(len(s_manager.groups))
        assert len(s_manager.groups) > 6

    def test_can_remove_key_from_group(self):
        s_manager = SecurityManager()
        s_manager.add_key_to_group(2, 1, 0)

        s_manager.remove_key_from_group(2, 1, 0)
        assert s_manager.groups[0].keys == set()
