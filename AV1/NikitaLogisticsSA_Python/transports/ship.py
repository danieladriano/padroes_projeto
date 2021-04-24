from transports.transport import Transport


class Ship(Transport):
    _cost: float = 0

    def __init__(self):
        self._cost = 9

    def deliver(self, distance: float) -> float:
        self.to_sail(distance)
        return distance * self._cost

    def to_sail(self, distance: float):
            print(f"Deliver by sea in a container. Distance {distance} Km.")
