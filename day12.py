import math
import re


def read_line(line: str) -> (str, int):
    action, amount = re.findall(r"([A-Z])(\d+)", line)[0]
    return action, int(amount)


def read_input(filename: str) -> [(str, int)]:
    with open(filename) as file:
        return [read_line(line) for line in file]


class Ship:
    def __init__(self, instructions: [(str, int)], start_dir: int = 90, start_coords: (int, int) = (0, 0)):
        self.instructions = instructions
        self.direction = start_dir
        self.coords = list(start_coords)  # (y,x)

    def update_position(self, instruction: (str, int)):
        direction, value = instruction
        if direction == 'N' or (direction == 'F' and self.direction == 0):
            self.coords[0] += value
        elif direction == 'S' or (direction == 'F' and self.direction == 180):
            self.coords[0] -= value
        elif direction == 'E' or (direction == 'F' and self.direction == 90):
            self.coords[1] += value
        elif direction == 'W' or (direction == 'F' and self.direction == 270):
            self.coords[1] -= value
        elif direction == 'R':
            self.direction += value
            self.direction %= 360
        elif direction == 'L':
            self.direction -= value
            self.direction %= 360

    def follow_instructions(self):
        for ins in self.instructions:
            self.update_position(ins)

    def get_manhattan_distance(self):
        return sum(abs(c) for c in self.coords)


class Ship2(Ship):
    def __init__(self, instructions: [(str, int)], start_dir: int = 90, start_coords: (int, int) = (0, 0),
                 waypoint_start: (int, int) = (1, 10)):
        super().__init__(instructions, start_dir, start_coords)
        self.waypoint = list(waypoint_start)  # (y,x)
        self.count = 0

    def update_position(self, instruction: (str, int)):
        direction, value = instruction
        if direction == 'F':
            self.coords[0] += value * self.waypoint[0]
            self.coords[1] += value * self.waypoint[1]
        elif direction == 'N':
            self.waypoint[0] += value
        elif direction == 'S':
            self.waypoint[0] -= value
        elif direction == 'E':
            self.waypoint[1] += value
        elif direction == 'W':
            self.waypoint[1] -= value
        elif direction == 'R':
            self.rotate_waypoint(-value)
        elif direction == 'L':
            self.rotate_waypoint(value)

    def rotate_waypoint(self, angle: int):
        angle = math.radians(angle)
        s = math.sin(angle)
        c = math.cos(angle)

        new_x = round(self.waypoint[1] * c - self.waypoint[0] * s)
        new_y = round(self.waypoint[1] * s + self.waypoint[0] * c)

        # print(f"Waypoint: {self.waypoint} -> {[new_y, new_x]}")
        self.waypoint = [new_y, new_x]


if __name__ == '__main__':
    input12 = read_input('input/day12')

    ship = Ship(input12)
    ship.follow_instructions()
    print(f"Puzzle 1: MH distance: {ship.get_manhattan_distance()}")

    ship = Ship2(input12)
    ship.follow_instructions()
    print(f"Puzzle 2: MH distance: {ship.get_manhattan_distance()}, coords: {ship.coords}, waypoint: {ship.waypoint}")
