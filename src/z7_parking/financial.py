from abc import ABC, abstractmethod

from src.z7_parking.errorz import ParkingSystemError


class IBillable(ABC):
    """
    Entities which can pay bills
    """

    @abstractmethod
    def pay(self, amount: float):
        raise NotImplementedError()


class IPaidService(ABC):
    """
    These services can charge IBillable clients fees.
    """

    @abstractmethod
    def requirePayment(self, billable: IBillable, amount: float):
        # billable.pay(amount)  # or sth. similar; take and collect the paid amount
        raise NotImplementedError()


class MonetaryParkingError(ParkingSystemError):
    pass
