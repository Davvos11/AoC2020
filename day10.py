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


def get_adapter_chain_arrangements(adapters: Set[int]) -> int:
    # Add wall and phone
    nodes = adapters.union({0, max(adapters) + 3})

    # Find all vertices between nodes
    vertices: Dict[int, Set[int]] = {}

    for a in nodes:
        for i in range(1, 4):
            if a + i in nodes:
                if a in vertices:
                    vertices[a].add(a+i)
                else:
                    vertices[a] = {a + i}

    # Find all parents of nodes
    parents: Dict[int, Set[int]] = {}
    for v in vertices:
        for child in vertices[v]:
            if child in parents:
                parents[child].add(v)
            else:
                parents[child] = {v}

    src = 0
    dest = max(nodes)

    # Initialise queue and visited list
    visited = {src}
    queue = [src]
    ways: Dict[int, int] = {0: 1}

    while queue:
        node = queue.pop()

        for next_node in sorted(vertices[node]):
            if next_node == dest:
                break
            if next_node not in visited:
                visited.add(next_node)
                w = 0
                for p in parents[next_node]:
                    w += ways[p]
                ways[next_node] = w
                queue.append(next_node)

    return ways[dest - 3]


if __name__ == '__main__':
    input10 = read_input('input/day10')

    t1 = time.time()
    puzzle1 = get_adapter_chain(input10)
    print(f"Puzzle 1: {puzzle1[1] * puzzle1[3]} (differences: {puzzle1})")
    print(f"   Time: {time.time() - t1}")

    t1 = time.time()
    puzzle2 = get_adapter_chain_arrangements(input10)
    print(f"\nPuzzle 2: {puzzle2}")
    print(f"   Time: {time.time() - t1}")
