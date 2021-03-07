import abc
from abstract_chair import AbstractChair
from abstract_table import AbstractTable


class FurnitureFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    @abc.abstractmethod
    def create_table(self) -> AbstractTable:
        pass
