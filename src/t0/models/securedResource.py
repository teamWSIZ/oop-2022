from dataclasses import dataclass


@dataclass
class SecuredResource:
    id: int
    name: str
    open: bool
