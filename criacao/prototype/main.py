import copy
from engine import Engine
from aircraft import Aircraft


def main():
    engine = Engine("Rolls-Royce Merlin")
    aircraft_1 = Aircraft(2, engine)
    aircraft_2 = copy.copy(aircraft_1)

    print(f"Aircraft 1 engine -> {aircraft_1.get_engine()}")
    print(f"Aircraft 1 engine type -> {aircraft_1.get_engine().get_engine_type()}")
    print(f"Aircraft 2 engine -> {aircraft_1.get_engine()}")
    print(f"Aircraft 2 engine type -> {aircraft_1.get_engine().get_engine_type()}")

    print("====================")

    aircraft_3 = copy.deepcopy(aircraft_1)
    aircraft_1.get_engine().set_engine_type("Rolls-Royce Merlin V12")
    print(f"Aircraft 1 engine -> {aircraft_1.get_engine()}")
    print(f"Aircraft 1 engine type -> {aircraft_1.get_engine().get_engine_type()}")
    print(f"Aircraft 3 engine -> {aircraft_3.get_engine()}")
    print(f"Aircraft 3 engine type -> {aircraft_3.get_engine().get_engine_type()}")

if __name__ == "__main__":
    main()
