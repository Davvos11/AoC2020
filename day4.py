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


if __name__ == '__main__':
    input4 = read_input('input/day4_test')
    print(input4)

