from house_builder import HouseBuilder


class ConstructionCompany():
    def __init__(self, builder):
        self._builder = builder

    def build_minimal_house(self):
        self._builder.build_walls()
        self._builder.build_roof()
        self._builder.build_doors()
        self._builder.build_windows()

    def build_house_with_garage(self):
        self.build_minimal_house()
        self._builder.build_garage()

    def build_house_with_swim_pool(self):
        self.build_house_with_garage()
        self._builder.build_swim_pool()
