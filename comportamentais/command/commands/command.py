import abc


class Command(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def execute(self):
        pass
