from furniture_factory import FurnitureFactory
from victorian_chair import VictorianChair
from victorian_table import VictorianTable


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_table(self) -> VictorianTable:
        return VictorianTable()
