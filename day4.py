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
        # Append the last passport
        passports.append(current_passport.strip())

    # Convert to booleans
    return passports


def validate_passport1(passport: str) -> bool:
    fields = re.findall(r"(\S+):(\S+)", passport)
    field_names = [f[0] for f in fields]
    return all([name in field_names for name in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])


def validate_passport2(passport: str) -> bool:
    fields = dict(re.findall(r"(\S+):(\S+)", passport))

    try:
        for name in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            value = fields[name]
            check_list = []

            if name == 'byr':
                check_list = [len(value) == 4, int(value) in range(1920, 2003)]
            elif name == 'iyr':
                check_list = [len(value) == 4, int(value) in range(2010, 2021)]
            elif name == 'eyr':
                check_list = [len(value) == 4, int(value) in range(2020, 2031)]
            elif name == 'hgt':
                height, unit = re.findall(r"(\d+)(\D+)", value)[0]
                if unit == 'cm':
                    r = 150, 194
                elif unit == 'in':
                    r = 59, 77
                else:
                    return False
                check_list = [int(height) in range(r[0], r[1])]
            elif name == 'hcl':
                check_list = [re.match(r"^#[a-f0-9]{6}$", value)]
            elif name == 'ecl':
                check_list = [value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']]
            elif name == 'pid':
                check_list = [re.match(r"^\d{9}$", value)]
            else:
                print(f"Unknown field: {name}:{value}")

            # Check if all the requirements for this field are met
            if not all(check_list):
                return False
    except (KeyError, IndexError):
        return False

    # If no KeyError (i.e. required field is not found), no IndexError (i.e. incorrect height formatting)
    #  and no checklist fail, the passport is valid
    return True


if __name__ == '__main__':
    input4 = read_input('input/day4')

    valid_count1 = valid_count2 = 0
    for passport in input4:
        if validate_passport1(passport):
            valid_count1 += 1
        if validate_passport2(passport):
            valid_count2 += 1

    print(f"Puzzle 1: {valid_count1} valid passports")
    print(f"Puzzle 2: {valid_count2} valid passports")

