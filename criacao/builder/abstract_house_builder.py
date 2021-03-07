import abc


class AbstractHouseBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def build_walls(self):
        pass

    @abc.abstractmethod
    def build_doors(self):
        pass

    @abc.abstractmethod
    def build_windows(self):
        pass

    @abc.abstractmethod
    def build_roof(self):
        pass

    @abc.abstractmethod
    def build_garage(self):
        pass

    @abc.abstractmethod
    def build_swim_pool(self):
        pass
