from dataclasses import dataclass
from uuid import uuid4, UUID


@dataclass
class User:
    name: str
    uid: UUID = None

    def __post_init__(self):
        self.uid = uuid4()


users = [User('Kadabra'), User('Zenek'), User('Ambroży')]
print(users)
users.sort(key=lambda u: u.uid)
print(users)
