import abc


class DeviceInterface(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def is_enable(self) -> bool:
        pass

    @abc.abstractclassmethod
    def enable(self):
        pass

    @abc.abstractclassmethod
    def disable(self):
        pass

    @abc.abstractclassmethod
    def get_volume(self) -> int:
        pass

    @abc.abstractclassmethod
    def set_volume(self, volume: int):
        pass

    @abc.abstractclassmethod
    def get_channel(self) -> int:
        pass

    @abc.abstractclassmethod
    def set_channel(self, channel: int):
        pass
