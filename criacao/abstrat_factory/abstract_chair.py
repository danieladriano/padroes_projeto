import abc


class AbstractChair(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sit_on(self):
        pass
