from road_logistics import RoadLogistics
from sea_logistics import SeaLogistics


def main(logistics):
    print(logistics.plan_delivery())

if __name__ == "__main__":
    print("Using trucks")
    main(RoadLogistics())
    print("Using ships")
    main(SeaLogistics())