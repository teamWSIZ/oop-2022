from random import randint

from src.t0.errors import SecurityUnauthorized, SecurityBadRequest
from src.t0.model import SecuredResource


class SecurityGroup:

    def __init__(self, group_id: int):
        self.__keys = set()
        self.__resources = set()
        self.__group_id = group_id

    def add_key(self, key_id: int):
        self.__keys.add(key_id)

    def remove_key(self, key_id: int):
        try:
            self.__keys.remove(key_id)
        except KeyError:
            pass

    def has_key(self, key_id: int) -> bool:
        return key_id in self.__keys

    def add_resource(self, resource_id: int):
        self.__resources.add(resource_id)

    def remove_resource(self, resource_id: int):
        try:
            self.__resources.remove(resource_id)
        except KeyError:
            pass

    def has_resource(self, resource_id: int) -> bool:
        return resource_id in self.__resources

    def get_group_id(self) -> int:
        return self.__group_id


class SecurityManager:

    def __init__(self):
        self.__sec_groups: dict[int, SecurityGroup] = dict()
        admin_group = SecurityGroup(0)
        admin_group.add_key(0)
        admin_group.add_resource(0)
        self.__sec_groups[0] = admin_group

    def add_key_to_group(self, executor_id: int, key_id: int, group_id: int):
        if not self.is_admin(executor_id):
            raise SecurityUnauthorized()

        self.__sec_groups[group_id].add_key(key_id)

    def remove_key_to_group(self, executor_id: int, key_id: int, group_id: int):
        if not self.is_admin(executor_id):
            raise SecurityUnauthorized()

        self.__sec_groups[group_id].remove_key(key_id)

    def add_resource_to_group(self, executor_id: int, resource_id: int, group_id: int):
        if not self.is_admin(executor_id):
            raise SecurityUnauthorized()

        self.__sec_groups[group_id].add_resource(resource_id)

    def remove_resource_to_group(self, executor_id: int, resource_id: int, group_id: int):
        if not self.is_admin(executor_id):
            raise SecurityUnauthorized()

        self.__sec_groups[group_id].remove_resource(resource_id)

    def check_key_opens_resource(self, key_id: int, resource_id: int) -> bool:
        for sg in self.__sec_groups.values():
            if sg.has_key(key_id) and sg.has_resource(resource_id):
                return True
        else:
            return False

    def create_group(self, executor_id=0) -> int:
        if not self.is_admin(executor_id):
            raise SecurityUnauthorized()

        unique_id = randint(1, 10 ** 6)
        while unique_id in self.__sec_groups.keys():
            unique_id = randint(1, 10 ** 6)
        group = SecurityGroup(unique_id)
        self.__sec_groups[unique_id] = group
        return unique_id

    def is_admin(self, key_id):
        return self.__sec_groups[0].has_key(key_id)


class LockManager:
    def __init__(self, security_manager: SecurityManager):
        self.__security_manager = security_manager
        self.__resources: dict[int, SecuredResource] = {}

    def lock(self, key_id: int, resource_id: int):
        self.__action(key_id, resource_id, desired_locked=True)

    def unlock(self, key_id: int, resource_id: int):
        self.__action(key_id, resource_id, desired_locked=False)

    def __action(self, key_id: int, resource_id: int, desired_locked: bool):
        if self.__security_manager.check_key_opens_resource(key_id, resource_id):
            if resource_id not in self.__resources:
                raise SecurityBadRequest('Resource not found')
            resource = self.__resources.get(resource_id)
            desired_unlock = not desired_locked
            if (resource.is_open and desired_locked) or (not resource.is_open and desired_unlock):
                resource.is_open = desired_unlock
            else:
                raise SecurityBadRequest('Resource already in desired state')
        else:
            raise SecurityUnauthorized(f'Key {key_id} is not authorized to lock/unlock {resource_id=}')

    def add_resource(self, resource: SecuredResource):
        # unsecured
        self.__resources[resource.resource_id] = resource

    def remove_resource(self, resource_id: int):
        self.__resources.pop(resource_id)

