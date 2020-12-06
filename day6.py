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
    input6 = read_input('input/day6')

    yes_count = 0
    for group in input6:
        yes_set = set()
        for person in group:
            for question in person:
                yes_set.add(question)

        yes_count += len(yes_set)

    print(f"Puzzle 1: {yes_count}")
