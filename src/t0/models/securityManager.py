from sesja.models.securityGroup import SecurityGroup
from sesja.errors.unauthorized import SecurityUnauthorized
import random


def check_executor_by_id(id: int) -> bool:
    """
    one of the best ideas I've ever seen
    :param id:
    :return bool:
    """
    return False if id % 2 == 0 else True


class SecurityManager:
    groups: dict[int, SecurityGroup]

    def __init__(self):
        self.groups = {0: SecurityGroup(0), 3: SecurityGroup(0)}

    def create_group_example(self) -> SecurityGroup | None:
        for _ in range(5):
            rand_gid = random.randint(2, 10 ** 7)
            self.groups[rand_gid] = SecurityGroup(gid=rand_gid)

        return self.groups[rand_gid]

    def remove_key_from_group(self, executor_id: int, key_id: int, group_id: int):
        if check_executor_by_id(executor_id):
            raise SecurityUnauthorized()
        self.groups.get(group_id).remove_key(key_id)

    def add_key_to_group(self, executor_id: int, key_id: int, group_id: int):
        if check_executor_by_id(executor_id):
            raise SecurityUnauthorized()
        group = self.groups.get(group_id)
        if group:
            self.groups.get(group_id).add_key(key_id)
        else:
            raise IndexError

    def remove_resource_from_group(self, executor_id: int, key_id: int, group_id: int):
        if check_executor_by_id(executor_id):
            raise SecurityUnauthorized()
        self.groups.get(group_id).remove_resource(key_id)

    def add_resource_to_group(self, executor_id: int, key_id: int, group_id: int):
        if check_executor_by_id(executor_id):
            raise SecurityUnauthorized()
        self.groups.get(group_id).add_resource(key_id)

    def check_key_opens_resource(self, key_id: int, resource_id: int) -> bool:
        for i in self.groups:
            if self.groups[i].has_key(key_id) and self.groups[i].has_key(resource_id):
                return True

        return False
