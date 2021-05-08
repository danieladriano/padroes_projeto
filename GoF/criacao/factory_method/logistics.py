import abc


class Logistics(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self) -> str:
        transport = self.create_transport()
        return transport.deliver()
