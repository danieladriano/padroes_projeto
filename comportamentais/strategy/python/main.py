from navigator import Navigator
from strategies.road_strategy import RoadStrategy
from strategies.public_transport_strategy import PublicTransportStrategy


def main():
    navigator = Navigator()

    print("1 - Carro")
    print("2 - Transporte publico")
    opcao = int(input("Opcao: "))

    if opcao == 1:
        strategy = RoadStrategy()
    else:
        strategy = PublicTransportStrategy()

    navigator.set_strategy(strategy)
    navigator.build_route("Beira-mar", "Estácio")

if __name__ == "__main__":
    main()
