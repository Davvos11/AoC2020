import re
from typing import Tuple, List

instructionType = Tuple[str, int]


def read_input(filename: str) -> [instructionType]:
    instructions = []
    # Lambda for casting the second parameter to an int
    convert = lambda t: (t[0], int(t[1]))

    # Read file
    with open(filename) as file:
        for line in file:
            instruction = re.findall(r"^(\w+) ([+-]\d+)", line.strip())[0]
            instructions.append(convert(instruction))

    return instructions


if __name__ == '__main__':
    input8 = read_input('input/day8_test')
    print(input8)
