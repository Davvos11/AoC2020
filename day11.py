import time
from functools import lru_cache
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


class SeatSolver:
    def __init__(self, seats: [[Seat or None]]):
        self.seats = seats
        self.adjacent_seats: Dict[Tuple[int, int], Set[Tuple[int, int]]] = {}
        self.occupied: Set[Tuple[int, int]] = set()

    def get_adjacent_seats(self, row: int, col: int) -> Set[Tuple[int, int]]:
        result = set()
        width = len(self.seats[0])
        height = len(self.seats)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    y = row - i
                    x = col - j
                    if 0 <= y < height and 0 <= x < width:
                        seat = self.seats[y][x]
                        if seat is not None:
                            result.add((y, x))
        return result

    def get_seats_occupied(self, coord_set: Set[Tuple[int, int]]) -> [bool]:
        result = []
        for i, j in coord_set:
            seat = self.seats[i][j]
            if seat is not None and seat['occupied']:
                result.append(seat)
        return result

    @staticmethod
    def apply_rule(seat: Seat, adj_seats_occ: int) -> (Seat, bool):
        # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        if not seat['occupied'] and adj_seats_occ == 0:
            return Seat(occupied=True), True
        # If a seat is occupied (#) and four or more seats adjacent to it are also occupied,
        # the seat becomes empty.
        elif seat['occupied'] and adj_seats_occ >= 4:
            return Seat(occupied=False), True
        # Otherwise, the seat's state does not change.
        else:
            return Seat(occupied=seat['occupied']), False

    def apply_rules(self) -> bool:
        result = []
        new_occupied: Set[Tuple[int, int]] = set()
        changed = False

        for i, row in enumerate(self.seats):
            result.append([])
            for j, seat in enumerate(row):
                if seat is None:
                    result[i].append(None)
                    continue

                if (i, j) not in self.adjacent_seats:
                    self.adjacent_seats[(i, j)] = self.get_adjacent_seats(i, j)

                adj_seats_occ = 0
                for s in self.adjacent_seats[(i, j)]:
                    if (s[0], s[1]) in self.occupied:
                        adj_seats_occ += 1

                new_seat, seat_changed = self.apply_rule(seat, adj_seats_occ)
                result[i].append(new_seat)
                if new_seat['occupied']:
                    new_occupied.add((i, j))
                if seat_changed:
                    changed = True

        self.occupied = new_occupied
        self.seats = result
        return changed

    def run(self) -> int:
        while True:
            changed = self.apply_rules()
            # Check if something changed
            if not changed:
                occupied = 0
                for row in self.seats:
                    for seat in row:
                        if seat is not None and seat['occupied']:
                            occupied += 1

                return occupied


class SeatSolver2(SeatSolver):
    def get_adjacent_seats(self, row: int, col: int) -> Set[Tuple[int, int]]:
        result = set()
        width = len(self.seats[0])
        height = len(self.seats)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    c = 1
                    while True:
                        # Check the next spot in "sight" until we find a seat
                        y = row - c*i
                        x = col - c*j
                        if 0 <= y < height and 0 <= x < width:
                            seat = self.seats[y][x]
                            if seat is not None:
                                result.add((y, x))
                                break
                            else:
                                c += 1
                        else:
                            break

        return result

    @staticmethod
    def apply_rule(seat: Seat, adj_seats_occ: int) -> (Seat, bool):
        # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        if not seat['occupied'] and not adj_seats_occ:
            return Seat(occupied=True), True
        # If a seat is occupied (#) and *five* or more seats adjacent to it are also occupied,
        # the seat becomes empty.
        elif seat['occupied'] and adj_seats_occ >= 5:
            return Seat(occupied=False), True
        # Otherwise, the seat's state does not change.
        else:
            return Seat(occupied=seat['occupied']), False


if __name__ == '__main__':
    input11: [[Seat or None]] = read_input('input/day11')

    t1 = time.time()
    solver = SeatSolver(input11)
    print(f"Puzzle 1: {solver.run()} seats ocupied")
    print(f"   Time: {time.time() - t1}s")

    t1 = time.time()
    solver = SeatSolver2(input11)
    print(f"Puzzle 1: {solver.run()} seats ocupied")
    print(f"   Time: {time.time() - t1}s")
