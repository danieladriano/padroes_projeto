from logistics import Logistics
from truck import Truck


class RoadLogistics(Logistics):
    def create_transport(self) -> Truck:
        return Truck()
