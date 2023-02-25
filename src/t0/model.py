from dataclasses import dataclass


@dataclass
class Key:
    key_id: int
    name: str


@dataclass
class SecuredResource:
    resource_id: int
    name: str
    is_open: bool = True

