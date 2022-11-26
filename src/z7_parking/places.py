from abc import abstractmethod, ABC

from src.z7_parking.vehicles import Vehicle


class IPlace(ABC):

    @abstractmethod
    def enter(self, vehicle: Vehicle):
        raise NotImplementedError()

    @abstractmethod
    def leave(self, vehicle: Vehicle):
        raise NotImplementedError()


class Parking(IPlace):

    def __init__(self):
        self.vehicles: set[Vehicle] = set()

    def enter(self, vehicle: Vehicle):
        self.vehicles.add(vehicle)

    def leave(self, vehicle: Vehicle):
        self.vehicles.remove(vehicle)


class TollParking(Parking):
    pass


if __name__ == '__main__':
    print('---')
    p = IPlace()
