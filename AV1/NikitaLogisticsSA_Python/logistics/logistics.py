import abc


class Logistics():
    def plan_delivery(self, distance: float) -> float:
        transport = self.get_transport()
        return transport.deliver(distance)

    @abc.abstractmethod
    def get_transport(self):
        pass
