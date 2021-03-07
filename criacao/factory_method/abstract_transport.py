import abc


class AbstractTransport(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def deliver(self) -> str:
        pass
