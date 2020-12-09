def read_input(filename: str) -> [int]:
    with open(filename) as file:
        return [int(line) for line in file]


if __name__ == '__main__':
    input9 = read_input('input/day9_test')
    print(input9)
