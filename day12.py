import re


def read_line(line: str) -> (str, int):
    action, amount = re.findall(r"([A-Z])(\d+)", line)[0]
    return action, int(amount)


def read_input(filename: str) -> [(str, int)]:
    with open(filename) as file:
        return [read_line(line) for line in file]


if __name__ == '__main__':
    input12 = read_input('input/day12')
    print(input12)
