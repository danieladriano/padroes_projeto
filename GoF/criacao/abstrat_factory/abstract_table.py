import abc


class AbstractTable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def has_legs(self):
        pass
