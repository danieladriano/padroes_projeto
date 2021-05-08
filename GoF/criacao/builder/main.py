from construction_company import ConstructionCompany
from house_builder import HouseBuilder


def main():
    house_builder = HouseBuilder()
    construction_company = ConstructionCompany(house_builder)

    print("Standard house")
    construction_company.build_minimal_house()
    house_builder.house.list_parts()

    print("House with garage")
    construction_company.build_house_with_garage()
    house_builder.house.list_parts()

    print("House with swimming pool")
    construction_company.build_house_with_swim_pool()
    house_builder.house.list_parts()

if __name__ == "__main__":
    main()
