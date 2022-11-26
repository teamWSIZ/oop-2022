# from src.z7_parking.places import Place


class Vehicle:
    def __init__(self):
        from src.z7_parking.places import IPlace
        self.place: IPlace = None
