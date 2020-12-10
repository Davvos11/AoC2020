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


def get_adapter_chain_arrangements(adapters: Set[int]) -> [[int]]:
    result: [[int]] = []
    target = max(adapters) + 3

    # Initialise empty queue (with start = 0)
    todo: [[int]] = [[0]]

    while len(todo) > 0:
        print(f"\rQueue: {len(todo)}", end="")
        # Continue with next chain from queue
        chain = todo.pop(0)
        current_joltage = chain[len(chain)-1]

        # Check all possible next adapters and add the new partial chain to the queue
        for i in range(1, 4):
            next_joltage = current_joltage + i
            if next_joltage in adapters:
                todo.append(chain + [next_joltage])

        # Check if we can reach the target
        if current_joltage >= target - 3:
            # Finish this branch
            result.append(chain)

    return result


if __name__ == '__main__':
    input10 = read_input('input/day10')

    t1 = time.time()
    puzzle1 = get_adapter_chain(input10)
    print(f"Puzzle 1: {puzzle1[1] * puzzle1[3]} (differences: {puzzle1})")
    print(f"   Time: {time.time() - t1}")

    t1 = time.time()
    puzzle2 = get_adapter_chain_arrangements(input10)
    print(f"\nPuzzle 2: {len(puzzle2)}")
    print(f"   Time: {time.time() - t1}")
