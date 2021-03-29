import abc


class NotifierInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send(self, message: str):
        pass
