# from __future__ import annotations
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from src.z7_parking.places import IPlace, VehicleFactory
# ↑↑ all these imports to avoid 'circular import' errors for types in signatures of methods
# https://mail.python.org/archives/list/python-dev@python.org/message/VIZEBX5EYMSYIJNDBF6DMUMZOCWHARSO/
from src.z7_parking.financial import IBillable


class Vehicle:

    def __init__(self):
        from src.z7_parking.places import IPlace, VehicleFactory  # repeated for variables
        self.place: IPlace = VehicleFactory()

    def move_to(self, place: 'IPlace'):  # this type hint will not be checked
        place.enter(self)


class Car(Vehicle):
    pass


class PremiumCar(Car, IBillable):

    def __init__(self, money: float = 10.0):
        super().__init__()
        self.money = money

    def pay(self, amount: float):
        self.money -= amount
