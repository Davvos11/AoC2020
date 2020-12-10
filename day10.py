import time
from typing import Set, Dict


def read_input(filename: str) -> Set[int]:
    with open(filename) as file:
        return {int(line) for line in file}


def get_adapter_chain(adapters: Set[int]) -> Dict[int, int]:
    current_joltage = 0
    differences = {1: 0, 2: 0, 3: 0}

    target = max(adapters) + 3

    while current_joltage < target - 3:
        # Check if there is an adaptor rated 1, then 2, then 3 jolt(s) higher
        for i in range(1, 4):
            if current_joltage + i in adapters:
                differences[i] += 1  # count difference
                current_joltage += i  # increase joltage
                break
    # Also count the difference between the final adapter and your phone
    differences[target - current_joltage] += 1
    return differences


if __name__ == '__main__':
    input10 = read_input('input/day10')

    t1 = time.time()
    puzzle1 = get_adapter_chain(input10)
    print(f"Puzzle 1: {puzzle1[1] * puzzle1[3]} (differences: {puzzle1})")
    print(f"   Time: {time.time() - t1}")

