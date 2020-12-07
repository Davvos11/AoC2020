import re
from typing import Dict, Set, Tuple, List

bagType = Dict[str, List[Tuple[int, str]]]


def read_input(filename: str) -> bagType:
    bags = {}

    # Read file
    with open(filename) as file:
        for line in file:
            line = line.strip()
            outer_bag = re.findall(r"(.+) bags contain", line)[0]
            inner_bags = re.findall(r"(\d+) ([\w|\s]+) bag", line)
            # Convert quantity to int before saving
            bags[outer_bag] = [(int(b[0]), b[1]) for b in inner_bags]

    return bags


def get_bags_containing(bags: bagType, bag_name: str) -> Set[str]:
    result = set()

    for bag in bags:
        # Check if the given bag name can be in this bag
        if bag_name in [b[1] for b in bags[bag]]:
            result.add(bag)
            # Also add all the bags that contain the outer bag (recursion)
            result |= get_bags_containing(bags, bag)

    return result


def count_bags_inside(bags: bagType, bag_name: str) -> int:
    result = 0

    for inner_bag in bags[bag_name]:
        result += inner_bag[0]
        # Also count the bags inside this bag (recursion)
        result += inner_bag[0] * count_bags_inside(bags, inner_bag[1])

    return result


if __name__ == '__main__':
    input7 = read_input('input/day7')

    print(f"Puzzle 1: {len(get_bags_containing(input7, 'shiny gold'))} bags")
    print(f"Puzzle 2: {count_bags_inside(input7, 'shiny gold')} bags")
