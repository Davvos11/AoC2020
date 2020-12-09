import time
from typing import Set, List


def read_input(filename: str) -> [int]:
    with open(filename) as file:
        return [int(line) for line in file]


def verify_number(number: int, preamble: List[int]) -> bool:
    for term1 in preamble:
        term2 = number - term1
        if term2 in preamble:
            return True
    return False


def find_incorrect_num(preamble_len: int, numbers: List[int]) -> int:
    preamble = []
    for i, number in enumerate(input9):
        # Create initial preamble
        if i < preamble_len:
            preamble.append(number)
            continue

        # For the rest of the input, verify each number
        if not verify_number(number, preamble):
            return number
        # And move the preamble set
        preamble = preamble[1::]
        preamble.append(number)


def find_cont_sum(target: int, numbers: List[int]) -> Set[int]:
    for i in range(len(numbers)):
        cont_set = set()

        # Add each next number to the set until the sum is either too big or correct
        for j in range(i, len(numbers)):
            cont_set.add(numbers[j])
            sum_value = sum(cont_set)

            if sum_value == target and len(cont_set) >= 2:
                return cont_set
            elif sum_value > target:
                break


if __name__ == '__main__':
    input9 = read_input('input/day9')

    t1 = time.time()
    puzzle1 = find_incorrect_num(25, input9)
    print(f"Puzzle 1: {puzzle1} does not follow the property")
    print(f"   Took: {(time.time() - t1)*1000}ms")

    t1 = time.time()
    puzzle2 = find_cont_sum(puzzle1, input9)
    min_int = min(puzzle2)
    max_int = max(puzzle2)
    print(f"Puzzle 2: {min_int + max_int} ({min_int} + {max_int})")
    print(f"   Took: {(time.time() - t1)*1000}ms")
