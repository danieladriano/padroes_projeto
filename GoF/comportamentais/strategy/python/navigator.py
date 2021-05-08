from strategies.route_strategy import RouteStrategy


class Navigator():
    _route_strategy: RouteStrategy = None

    def set_strategy(self, strategy: RouteStrategy):
        self._route_strategy = strategy

    def build_route(self, point_a, point_b):
        self._route_strategy.build_route(point_a, point_b)
