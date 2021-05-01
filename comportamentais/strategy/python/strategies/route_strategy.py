import abc


class RouteStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def build_route(self, point_a, point_b):
        pass
