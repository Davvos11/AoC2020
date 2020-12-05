import re

seatType = (int, int, int)


def bin_string_to_int(string: str, length: int, lower: str, upper: str) -> int:
    # Create list of potential ints
    ints = range(length)
    for char in string:
        length = len(ints)
        # Decide which half to keep
        if char == lower:
            ints = ints[0:length//2]
        elif char == upper:
            ints = ints[length//2:]
        else:
            print(f"Unsupported char: {char} (valid: {lower} or {upper})")
    # We should only have one int left in the list by now
    return ints.start


def line_to_seat(line: str) -> seatType:
    row_string, col_string = re.findall(r"([FB]+)([LR]+)", line)[0]

    row = bin_string_to_int(row_string, 128, 'F', 'B')
    col = bin_string_to_int(col_string, 8, 'L', 'R')

    return row, col, 8*row + col


def read_input(filename: str) -> [seatType]:
    # Read file
    with open(filename) as file:
        return [line_to_seat(line.strip()) for line in file]


if __name__ == '__main__':
    input5 = read_input('input/day5')
    seat_ids = [x[2] for x in input5]

    print(f"Puzzle 1: {max(seat_ids)}")

    # Get a set of empty seats
    empty_seats = set(range(8*127+7)) - set(seat_ids)
    # Check for each seat if their neighbours are also empty, if not: we got our seat
    for seat in list(empty_seats):
        # Special cases for highest and lowest index:
        if seat == 0 or seat == max(empty_seats):
            # Just ignore them since it was given that those aren't our seat
            continue
        else:
            if not (seat - 1 in empty_seats) and not (seat + 1 in empty_seats):
                print(f"Puzzle 2: {seat}")
