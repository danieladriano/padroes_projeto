from abstract_transport import AbstractTransport


class Truck(AbstractTransport):
    def deliver(self) -> str:
        return "Deliver by roads in a box"
