from logistics.logistics import Logistics
from transports.truck import Truck


class RoadLogistics(Logistics):
    def get_transport(self) -> Truck:
        return Truck()
