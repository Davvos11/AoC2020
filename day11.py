import time
from typing import TypedDict, Dict, List, Set, Tuple


class Seat(TypedDict):
    occupied: bool


def read_line(line: str) -> [Seat or None]:
    result = []
    for char in line.strip():
        if char == '.':
            result.append(None)
        elif char == 'L':
            result.append(Seat(occupied=False))
        elif char == '#':
            result.append(Seat(occupied=False))
        else:
            print(f"Unexpected input: {char}")
    return result


def read_input(filename: str) -> [[Seat or None]]:
    # Read file
    with open(filename) as file:
        return [read_line(line) for line in file]


def get_adjacent_seats(seats: [[Seat or None]], row: int, col: int) -> Set[Tuple[int, int]]:
    result = set()
    width = len(seats[0])
    height = len(seats)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                y = row - i
                x = col - j
                if 0 <= y < height and 0 <= x < width:
                    seat = seats[y][x]
                    if seat is not None:
                        result.add((y, x))
    return result


def get_seats_occupied(seats: [[Seat or None]], coord_set: Set[Tuple[int, int]]) -> [bool]:
    result = []
    for i, j in coord_set:
        seat = seats[i][j]
        if seat is not None and seat['occupied']:
            result.append(seat)
    return result


def apply_rules(seats: [[Seat or None]], adjacent_seats: Dict[Tuple[int, int], Set[Tuple[int, int]]]) -> ([[Seat or None]], bool):
    result = []
    changed = False

    for i, row in enumerate(seats):
        result.append([])
        for j, seat in enumerate(row):
            if seat is None:
                result[i].append(None)
                continue

            if (i, j) not in adjacent_seats:
                adjacent_seats[(i, j)] = get_adjacent_seats(seats, i, j)
            adj_seats_occ = get_seats_occupied(seats, adjacent_seats[(i, j)])

            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if not seat['occupied'] and not any(adj_seats_occ):
                changed = True
                result[i].append(Seat(occupied=True))
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            elif seat['occupied'] and len(adj_seats_occ) >= 4:
                changed = True
                result[i].append(Seat(occupied=False))
            # Otherwise, the seat's state does not change.
            else:
                result[i].append(Seat(occupied=seat['occupied']))
    return result, changed


if __name__ == '__main__':
    input11: [[Seat or None]] = read_input('input/day11')

    t1 = time.time()

    adjacent_seats: Dict[Tuple[int, int], Set[Tuple[(int, int)]]] = {}
    while True:
        input11, changed = apply_rules(input11, adjacent_seats)
        # Check if something changed
        if not changed:
            occupied = 0
            for row in input11:
                for seat in row:
                    if seat is not None and seat['occupied']:
                        occupied += 1

            print(f"Puzzle 1: {occupied} seats ocupied")
            break

    print(f"   Time: {time.time() - t1}s")
