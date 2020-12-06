def read_input(filename: str) -> [str]:
    groups = []
    current_group = []

    # Read file
    with open(filename) as file:
        for line in file:
            line = line.strip()
            # If this is a blank line, go to the next passport
            if line == "":
                groups.append(current_group)
                current_group = []
            else:
                current_group.append(list(line.strip()))
        # Append the last passport
        groups.append(current_group)

    # Convert to booleans
    return groups


if __name__ == '__main__':
    input6 = read_input('input/day6_test')
    print(input6)
