from transports.transport import Transport


class Truck(Transport):
    _cost: float = 0

    def __init__(self):
        self._cost = 10

    def deliver(self, distance: float) -> float:
        self.to_drive(distance)
        return distance * self._cost

    def to_drive(self, distance: float):
            print(f"Deliver by roads in a box. Distance: {distance} Km.")
