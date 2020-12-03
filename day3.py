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


def count_trees(trees: [[bool]], right, down):
    x = y = tree_count = 0
    # Loop until we reached the bottom
    while y < len(trees):
        # Check if there is a tree in this position
        if contains_tree(trees, x, y):
            tree_count += 1
        # Go to the next position
        x += right
        y += down
    return tree_count


if __name__ == '__main__':
    input3 = read_input('input/day3')

    print(f"Puzzle 1: {count_trees(input3, 3, 1)} trees")

    print("\nPuzzle 2:")
    puzzle2 = 1
    for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        count = count_trees(input3, r, d)
        puzzle2 *= count
        print(f"   right {r}, down {d}: {count} trees")
    print(f"Result: {puzzle2}")
