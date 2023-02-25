from sesja.models.securityManager import SecurityManager
from sesja.errors.securityBadRequest import SecurityBadRequest


class LockManager:
    secmgr: SecurityManager

    def __init__(self, securitymanager_instance: SecurityManager) -> None:
        self.secmgr = securitymanager_instance

    def lock(self, key_id: int, resource_id: int):
        raise SecurityBadRequest()

    def unlock(self, key_id: int, resource_id: int):
        raise SecurityBadRequest()
