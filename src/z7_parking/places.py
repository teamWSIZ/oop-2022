from src.z7_parking.common import *
from src.z7_parking.financial import IPaidService, IBillable, MonetaryParkingError
from src.z7_parking.vehicles import *
from src.z7_parking.errorz import *


class IPlace(ABC):

    @abstractmethod
    def enter(self, vehicle: Vehicle):
        raise NotImplementedError()

    @abstractmethod
    def leave(self, vehicle: Vehicle):
        raise NotImplementedError()


class VehicleFactory(IPlace):

    def enter(self, vehicle: Vehicle):
        pass

    def leave(self, vehicle: Vehicle):
        print('Have a good (vehicle) life!')


class Parking(IPlace, IFixedCapacity):

    def __init__(self, max_capacity=10):
        self.vehicles: set[Vehicle] = set()
        self.max_capacity = max_capacity

    def get_max_capacity(self) -> int:
        return self.max_capacity

    def get_free_capacity(self) -> int:
        return self.max_capacity - len(self.vehicles)

    def enter(self, vehicle: Vehicle):
        if vehicle in self.vehicles:
            raise ParkingSystemError('Cannot reenter parking')
        if self.get_free_capacity() == 0:
            raise ParkingFullError(f'The Parking {self.get_max_capacity()} is fully occupied')

        self.vehicles.add(vehicle)
        vehicle.place.leave(vehicle)  # vehicel must leave its previous place

        vehicle.place = self

    def leave(self, vehicle: Vehicle):
        if vehicle not in self.vehicles:
            raise ParkingSystemError('Cannot leave Parking; vehicle not present there')

        print(f'vehicle {vehicle} leaves place {self}')
        self.vehicles.remove(vehicle)


class TollParking(Parking, IPaidService):
    def __init__(self, fee_per_second=1):
        super().__init__()
        self.account_balance = 0  # initial amount of money of the parking
        self.fee_per_second = fee_per_second

    def enter(self, vehicle: Vehicle):
        # print('bases:', vehicle.__class__.mro())  # todo: important -- all base classes; method resolution order
        # print(vehicle.__class__.__bases__)  # todo: direct bases

        if not issubclass(vehicle.__class__, IBillable):
            raise MonetaryParkingError('Non-billable vehicle cannot enter or leave TollParking')

    def leave(self, vehicle: Vehicle):
        print('leaving toll parking')
        if not issubclass(vehicle.__class__, IBillable):
            raise ParkingSystemError('Non-billable vehicle cannot enter or leave TollParking')

        parking_duration = 2  # todo: setup proper time measurement for each IBillable
        amount = parking_duration * self.fee_per_second
        self.requirePayment(vehicle, amount)

        return super().leave(vehicle)  # standard action for an instance of Vehicle

    def requirePayment(self, billable: IBillable, amount: float):
        billable.pay(amount)
        self.account_balance += amount
