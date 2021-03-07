from abstract_house_builder import AbstractHouseBuilder
from house import House


class HouseBuilder(AbstractHouseBuilder):
    def __init__(self):
        self.reset()

    @property
    def house(self) -> House:
        house = self._house
        self.reset()
        return house

    def reset(self):
        self._house = House()

    def build_walls(self):
        self._house.add("Walls")

    def build_doors(self):
        self._house.add("Doors")

    def build_windows(self):
        self._house.add("Windows")

    def build_roof(self):
        self._house.add("Roof")

    def build_garage(self):
        self._house.add("Garage")

    def build_swim_pool(self):
        self._house.add("SwimPool")

