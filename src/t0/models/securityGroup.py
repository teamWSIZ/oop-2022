class SecurityGroup:
    keys: set[int]
    resources: set[int]
    group_id: int

    def __init__(self, gid: int):
        self.keys = set()
        self.resources = set()
        self.group_id = gid

    # Keys
    def add_key(self, key_id: int):
        self.keys.add(key_id)

    def remove_key(self, key_id: int):
        self.keys.remove(key_id)

    def has_key(self, key_id: int) -> bool:
        return key_id in self.keys

    # Resource
    def add_resource(self, resource_id: int):
        self.resources.add(resource_id)

    def remove_resource(self, resource_id: int):
        self.resources.remove(resource_id)

    def has_resource(self, resource_id: int) -> bool:
        return resource_id in self.resources
