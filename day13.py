import math


def read_input(filename: str) -> (int, [int]):
    with open(filename) as file:
        timestamp = int(file.readline())
        schedule = [int(b) for b in file.readline().split(",") if b != 'x']
        return timestamp, schedule


def closest_bus(timestamp: int, busses: [int]):
    closest: (int, int) = None  # (id, eta)
    # Loop through busses
    for bus in busses:
        eta = bus - timestamp % bus
        # If we found a shorter wait time, update the result
        if closest is None or closest[1] > eta:
            closest = (bus, eta)

    return closest


if __name__ == '__main__':
    input13 = read_input('input/day13')

    puzzle1 = closest_bus(input13[0], input13[1])
    print(f"Part 1: {math.prod(puzzle1)} (closest bus: {puzzle1[0]} in {puzzle1[1]} minutes)")
