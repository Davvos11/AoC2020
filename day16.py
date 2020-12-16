import re
from typing import Set


def read_fields(fields: str) -> [(str, Set[int])]:
    result = []
    for match in re.findall(r"(\w+): (\d+)-(\d+) or (\d+)-(\d+)", fields, re.MULTILINE):
        valid = set(range(int(match[1]), int(match[2]) + 1)).union(set(range(int(match[3]), int(match[4]) + 1)))
        result.append((match[0], valid))
    return result


def read_tickets(tickets: str) -> [[int]]:
    result = []
    for ticket in tickets.split('\n'):
        result.append([int(field) for field in ticket.split(',')])
    return result


def read_input(filename: str):
    with open(filename) as file:
        fields, your_ticket, nearby_tickets = \
            re.findall(r"(.+)\n\nyour ticket:\n(.+)\n\nnearby tickets:\n(.+)", file.read(), re.DOTALL)[0]

    return read_fields(fields), read_tickets(your_ticket)[0], read_tickets(nearby_tickets)


if __name__ == '__main__':
    input16 = read_input('input/day16_test')
    print(input16)



