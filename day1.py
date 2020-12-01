import time


def read_input(filename: str) -> [int]:
    # Read file
    with open(filename) as file:
        lines = file.readlines()
    # Convert to ints
    return [int(line) for line in lines]


def find_sum(entries: [int], sum_value: int) -> (int, int):
    for entry in entries:
        other_entry = sum_value - entry
        if other_entry in entries:
            return entry, other_entry


def find_sum3(entries: [int], sum_value: int) -> (int, int, int):
    for entry1 in entries:
        for entry2 in entries:
            other_entry = sum_value - entry1 - entry2
            if other_entry in entries:
                return entry1, entry2, other_entry


if __name__ == '__main__':
    input1 = read_input('input/day1')

    time_a = time.time()
    solution1 = find_sum(input1, 2020)
    time_b = time.time()

    print(f"Part 1 ({time_b -time_a}s)")
    print(solution1)
    print(solution1[0] * solution1[1])

    time_a = time.time()
    solution2 = find_sum3(input1, 2020)
    time_b = time.time()

    print(f"\nPart 2 ({time_b -time_a}s)")
    print(solution2)
    print(solution2[0] * solution2[1] * solution2[2])

