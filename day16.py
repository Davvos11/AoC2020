import math
import re
from typing import Set


def read_fields(fields: str) -> [(str, Set[int])]:
    result = []
    for match in re.findall(r"([ \w]+): (\d+)-(\d+) or (\d+)-(\d+)", fields, re.MULTILINE):
        valid = set(range(int(match[1]), int(match[2]) + 1)).union(set(range(int(match[3]), int(match[4]) + 1)))
        result.append((match[0], valid))
    return result


def read_tickets(tickets: str) -> [[int]]:
    result = []
    for ticket in tickets.split('\n'):
        result.append([int(field) for field in ticket.split(',')])
    return result


def read_input(filename: str) -> ([(str, Set[int])], [int], [[int]]):
    with open(filename) as file:
        fields, your_ticket, nearby_tickets = \
            re.findall(r"(.+)\n\nyour ticket:\n(.+)\n\nnearby tickets:\n(.+)", file.read().strip(), re.DOTALL)[0]

    return read_fields(fields), read_tickets(your_ticket)[0], read_tickets(nearby_tickets)


def get_invalid_ticket_rate(rules: [(str, Set[int])], tickets: [[int]]) -> int:
    rate = 0
    all_valid_values = set().union(*[r[1] for r in rules])
    for ticket in tickets:
        for value in ticket:
            if value not in all_valid_values:
                rate += value
    return rate


def get_valid_tickets(rules: [(str, Set[int])], tickets: [[int]]) -> [[int]]:
    all_valid_values = set().union(*[r[1] for r in rules])
    result = tickets.copy()
    for ticket in tickets:
        for value in ticket:
            if value not in all_valid_values:
                result.remove(ticket)
                break
    return result


def find_fields(rules: [(str, Set[int])], tickets: [[int]]) -> [str]:
    field_count = len(tickets[0])
    fields = [None for _ in range(field_count)]
    rules_c = rules.copy()

    while None in fields:
        for i, field in enumerate([{tickets[i][j] for i in range(len(tickets))} for j in range(field_count)]):
            valid_rules: [str] = []
            for rule in rules_c:
                # Check if this field has no values that are not in this rule
                if len(field.difference(rule[1])) == 0:
                    valid_rules.append(rule)
            # If there is only one rule that is valid for this field, assign it
            if len(valid_rules) == 1:
                fields[i] = valid_rules[0][0]
                rules_c.remove(valid_rules[0])

    return fields


if __name__ == '__main__':
    input16 = read_input('input/day16')

    print(f"Puzzle 1: error rate: {get_invalid_ticket_rate(input16[0], input16[2])}")

    valid_tickets = get_valid_tickets(input16[0], input16[2])
    field_names = find_fields(input16[0], valid_tickets)
    print(f"Puzzle 2: field_names: {field_names}")
    departures = [input16[1][i] for i, name in enumerate(field_names) if str(name).startswith("departure")]
    puzzle2 = math.prod(departures) if len(departures) > 0 else 0
    print(f"    Answer: {puzzle2}")
