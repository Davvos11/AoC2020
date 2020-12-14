def read_input(filename: str) -> (int, [int]):
    with open(filename) as file:
        timestamp = int(file.readline())
        schedule = [int(b) for b in file.readline().split(",") if b != 'x']
        return timestamp, schedule


if __name__ == '__main__':
    input13 = read_input('input/day13_test')
    print(input13)
