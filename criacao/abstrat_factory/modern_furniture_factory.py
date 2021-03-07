from furniture_factory import FurnitureFactory
from modern_chair import ModernChair
from modern_table import ModernTable


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> ModernChair:
        return ModernChair()

    def create_table(self) -> ModernTable:
        return ModernTable()
