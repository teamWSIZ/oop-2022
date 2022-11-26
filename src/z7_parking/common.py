from abc import ABC, abstractmethod


class IFixedCapacity(ABC):

    @abstractmethod
    def get_max_capacity(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def get_free_capacity(self) -> int:
        raise NotImplementedError()


class ParkingError(RuntimeError):
    """
    General errors in the parking system
    """
    pass


class OutOfCapacityParkingError(ParkingError):
    pass
