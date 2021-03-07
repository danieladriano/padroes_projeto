from abstract_transport import AbstractTransport


class Ship(AbstractTransport):
    def deliver(self) -> str:
        return "Deliver by sea in a container"
