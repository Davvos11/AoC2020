
def read_line(line: str) -> [bool]:
    return [char == '#' for char in line.strip()]


def read_input(filename: str) -> [[bool]]:
    # Read file
    with open(filename) as file:
        lines = file.readlines()
    # Convert to booleans
    return [read_line(line) for line in lines]


def contains_tree(trees: [[bool]], x: int, y: int) -> bool:
    row = trees[y]
    return row[x % len(row)]


if __name__ == '__main__':
    input3 = read_input('input/day3')

    x = y = tree_count = 0
    # Loop until we reached the bottom
    while y < len(input3):
        # Check if there is a tree in this position
        if contains_tree(input3, x, y):
            tree_count += 1
        # Go to the next position
        x += 3
        y += 1

    print(f"Puzzle 1: {tree_count} trees")
