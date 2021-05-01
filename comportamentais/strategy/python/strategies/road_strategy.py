from strategies.route_strategy import RouteStrategy


class RoadStrategy(RouteStrategy):
    def build_route(self, point_a, point_b):
        print(f"Roteiro do {point_a} até {point_b} utilizando carro!")
