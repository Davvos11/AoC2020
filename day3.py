
def read_line(line: str) -> [bool]:
    return [char == '#' for char in line]


def read_input(filename: str) -> [[bool]]:
    # Read file
    with open(filename) as file:
        lines = file.readlines()
    # Convert to booleans
    return [read_line(line) for line in lines]


def contains_tree(trees: [[bool]], y: int, x: int) -> bool:
    row = trees[y]
    return row[x % len(row)]


if __name__ == '__main__':
    input3 = read_input('input/day3')
    print(contains_tree(input3, 0, 4))
    print(contains_tree(input3, 0, 8))
    print(contains_tree(input3, 0, 8+32*10))
