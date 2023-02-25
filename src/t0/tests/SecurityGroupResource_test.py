import unittest
import random
from sesja.models.securityGroup import SecurityGroup
from sesja.models.key import Key
from sesja.models.securedResource import SecuredResource


class SecurityTests(unittest.TestCase):

    def test_can_add_key(self):
        group = SecurityGroup(random.randint(1, 10 ** 7))
        key = Key(1, "MARY'S KEY")
        group.add_key(key.id)
        assert group.has_key(key.id) is True

    def test_can_remove_key(self):
        group = SecurityGroup(random.randint(1, 10 ** 7))
        key = Key(1, "MARY'S KEY")
        assert group.has_key(key.id) is False

    def test_can_add_resource(self):
        group = SecurityGroup(random.randint(1, 10 ** 7))
        door = SecuredResource(1, "main_door", False)
        group.add_resource(door.id)
        assert group.has_resource(door.id) is True

    def test_can_remove_resource(self):
        group = SecurityGroup(random.randint(1, 10 ** 7))
        door = SecuredResource(1, "main_door", False)
        assert group.has_resource(door.id) is False

