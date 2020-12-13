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
        self.coords = list(start_coords)  # (x,y)

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


if __name__ == '__main__':
    input12 = read_input('input/day12')

    ship = Ship(input12)
    ship.follow_instructions()
    print(f"Puzzle 1: MH distance: {ship.get_manhattan_distance()}")
