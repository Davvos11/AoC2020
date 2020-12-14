import math
import time
from functools import reduce


def read_input(filename: str) -> (int, [int or None]):
    with open(filename) as file:
        timestamp = int(file.readline())
        schedule = [int(b) if b != 'x' else None for b in file.readline().split(",")]
        return timestamp, schedule


def closest_bus(timestamp: int, busses: [int or None]) -> (int, int):
    closest: (int, int) = None  # (id, eta)
    # Loop through busses
    for bus in busses:
        if bus is None:
            continue
        eta = bus - timestamp % bus
        # If we found a shorter wait time, update the result
        if closest is None or closest[1] > eta:
            closest = (bus, eta)

    return closest


# De gejatte code de nice
# https://rosettacode.org/wiki/Chinese_remainder_theorem
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def find_subsequent_busses(busses: [int or None]) -> int:
    n = [b for b in busses if b is not None]
    a = [b - i for i, b in enumerate(busses) if b is not None]

    return chinese_remainder(n, a)


if __name__ == '__main__':
    input13 = read_input('input/day13')

    t1 = time.time()
    puzzle1 = closest_bus(input13[0], input13[1])
    print(f"Part 1: {math.prod(puzzle1)} (closest bus: {puzzle1[0]} in {puzzle1[1]} minutes)")
    print(f"    Time: {(time.time() - t1) * 1000} ms\n")

    for test in range(1, 7):
        test_input = read_input(f'input/day13_test{test}')
        t1 = time.time()
        puzzle2 = find_subsequent_busses(test_input[1])
        print(f"      Part 2 test {test}: timestamp: {puzzle2}\t {puzzle2 == test_input[0]}")
        print(f"          Time: {(time.time() - t1) * 1000} ms")

    t1 = time.time()
    puzzle2 = find_subsequent_busses(input13[1])
    print(f"Part 2: timestamp: {puzzle2}")
    print(f"    Time: {(time.time() - t1) * 1000} ms")

