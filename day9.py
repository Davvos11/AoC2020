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


PREAMBLE_LEN = 25

if __name__ == '__main__':
    input9 = read_input('input/day9')

    preamble = []
    for i, number in enumerate(input9):
        # Create initial preamble
        if i < PREAMBLE_LEN:
            preamble.append(number)
            continue

        # For the rest of the input, verify each number
        if not verify_number(number, preamble):
            print(f"Puzzle 1: {number} does not follow the property")
            break
        # And move the preamble set
        preamble = preamble[1::]
        preamble.append(number)
