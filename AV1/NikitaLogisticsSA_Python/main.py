from logistics.logistics import Logistics
from logistics.road_logistics import RoadLogistics
from logistics.sea_logistics import SeaLogistics

class App():
    def __init__(self, logistics: Logistics):
        self._logistics = logistics

    def run(self, distance: float):
        cost = self._logistics.plan_delivery(distance)
        print(f"Transport cost ${cost}")

if __name__ == "__main__":
    road = RoadLogistics()
    app = App(road)
    app.run(500)

    print("--------------")

    sea = SeaLogistics()
    app = App(sea)
    app.run(5000)
