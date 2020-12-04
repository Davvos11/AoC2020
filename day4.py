import re


def read_input(filename: str) -> [str]:
    passports = []
    current_passport = ""

    # Read file
    with open(filename) as file:
        for line in file:
            line = line.strip()
            # If this is a blank line, go to the next passport
            if line == "":
                passports.append(current_passport.strip())
                current_passport = ""
            else:
                current_passport += line + " "

    # Convert to booleans
    return passports


def validate_passport(passport: str) -> bool:
    fields = re.findall(r"(\S+):(\S+)", passport)
    field_names = [f[0] for f in fields]
    return all([name in field_names for name in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])


if __name__ == '__main__':
    input4 = read_input('input/day4')

    valid_count = 0
    for passport in input4:
        if validate_passport(passport):
            valid_count += 1

    print(f"Puzzle 1: {valid_count} valid passports")

