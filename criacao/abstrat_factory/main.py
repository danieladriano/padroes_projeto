from victorian_furniture_factory import VictorianFurnitureFactory
from modern_furniture_factory import ModernFurnitureFactory

def main(factory):
    chair = factory.create_chair()
    chair.sit_on()

    table = factory.create_table()
    table.has_legs()

if __name__ == "__main__":
    print("Create Victorian Furniture")
    main(VictorianFurnitureFactory())

    print("Create Modern Furniture")
    main(ModernFurnitureFactory())
