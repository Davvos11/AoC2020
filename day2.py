import re
from typing import Iterable


def read_line(line: str) -> (int, int, str, str):
    match = re.findall(r"(\d+)-(\d+) (\w): (.*)", line)[0]
    return int(match[0]), int(match[1]), match[2], match[3]


def read_input(filename: str) -> [(int, int, str, str)]:
    # Read file
    with open(filename) as file:
        lines = file.readlines()
    # Convert to tuples
    return [read_line(line) for line in lines]


if __name__ == '__main__':
    input2 = read_input('input/day2')
    print(input2[0:5])
