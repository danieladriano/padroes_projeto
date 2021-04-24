import abc


class Transport(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def deliver(self, distance: float) -> float:
        pass
