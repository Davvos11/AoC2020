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


if __name__ == '__main__':
    input1 = read_input('input/day1')
    solution1 = find_sum(input1, 2020)
    print(solution1)
    print(solution1[0] * solution1[1])

