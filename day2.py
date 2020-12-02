import re

entryType = (int, int, str, str)


def read_line(line: str) -> entryType:
    match = re.findall(r"(\d+)-(\d+) (\w): (.*)", line)[0]
    return int(match[0]), int(match[1]), match[2], match[3]


def read_input(filename: str) -> [entryType]:
    # Read file
    with open(filename) as file:
        lines = file.readlines()
    # Convert to tuples
    return [read_line(line) for line in lines]


def check_password1(entry: entryType) -> bool:
    # entry[3] should contain at least entry[0] and at most entry[1] of entry[2]
    return entry[3].count(entry[2]) in range(entry[0], entry[1]+1)


def check_password2(entry: entryType) -> bool:
    # entry[3] should have entry[2] at either index entry[0]-1 or entry[1]-1 (not both)
    char1 = entry[3][entry[0] - 1] == entry[2]
    char2 = entry[3][entry[1] - 1] == entry[2]
    # xor
    return char1 ^ char2


if __name__ == '__main__':
    input2 = read_input('input/day2')

    valid = 0
    for e in input2:
        if check_password1(e):
            valid += 1
    print(f"Puzzle 1: {valid} valid passwords")

    valid = 0
    for e in input2:
        if check_password2(e):
            valid += 1
    print(f"Puzzle 2: {valid} valid passwords")
