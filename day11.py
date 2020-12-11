from typing import TypedDict


class Seat(TypedDict):
    occupied: bool


def read_line(line: str) -> [Seat or None]:
    result = []
    for char in line.strip():
        if char == '.':
            result.append(None)
        elif char == 'L':
            result.append(Seat(occupied=False))
        elif char == '#':
            result.append(Seat(occupied=False))
        else:
            print(f"Unexpected input: {char}")
    return result


def read_input(filename: str) -> [[Seat or None]]:
    # Read file
    with open(filename) as file:
        return [read_line(line) for line in file]


if __name__ == '__main__':
    input11 = read_input('input/day11_test')
    print(input11[1])
