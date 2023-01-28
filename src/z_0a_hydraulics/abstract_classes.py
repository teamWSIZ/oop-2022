from abc import ABC, abstractmethod


class DontCreateInstances(ABC):

    @abstractmethod
    def __init__(self):
        print('should not work')


a = DontCreateInstances()