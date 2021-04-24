from logistics.logistics import Logistics
from transports.ship import Ship


class SeaLogistics(Logistics):
    def get_transport(self) -> Ship:
        return Ship()
