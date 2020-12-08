import re
from typing import Tuple, List

instructionType = Tuple[str, int]


def read_input(filename: str) -> [instructionType]:
    instructions = []
    # Lambda for casting the second parameter to an int
    convert = lambda t: (t[0], int(t[1]))

    # Read file
    with open(filename) as file:
        for line in file:
            instruction = re.findall(r"^(\w+) ([+-]\d+)", line.strip())[0]
            instructions.append(convert(instruction))

    return instructions


class Console:
    def __init__(self, instructions: [instructionType]):
        self.instructions = instructions
        self.accumulator = 0
        self.pc = 0
        self.executed_instructions: List[int] = []
        self.completed = False

    def run(self):
        while True:
            # Stop if we are running an instruction that we already have run before
            if self.pc in self.executed_instructions:
                break
            # If we reached the end of our program, we can also finish
            if self.pc >= len(self.instructions):
                self.completed = True
                break

            # Add the counter of the instruction to the list
            self.executed_instructions.append(self.pc)

            ins = self.instructions[self.pc]
            if ins[0] == 'acc':
                self.accumulator += ins[1]
            elif ins[0] == 'jmp':
                self.pc += ins[1]
            elif ins[0] == 'nop':
                pass
            else:
                print(f"Unknown operation {ins}")

            # Unless 'jmp' already increased it, increase the program counter
            if ins[0] != 'jmp':
                self.pc += 1


if __name__ == '__main__':
    input8 = read_input('input/day8')

    console = Console(input8)
    console.run()
    print(f"Puzzle 1: accumulator value = {console.accumulator}")

    # Get a list of instruction-indices of the jmp and nop instructions
    jmp_accs = [i for i, ins in enumerate(input8) if ins[0] in ['nop', 'jmp']]
    # Lambda to change a jmp to nop
    modify = lambda ins: ('nop' if ins[0] == 'jmp' else 'jmp', ins[1])

    # It's bruteforce time everybody
    for i in jmp_accs:
        # Change a jmp to a nop or vice versa
        new_ins = input8.copy()
        new_ins[i] = modify(new_ins[i])
        # Check if the program terminates
        console = Console(new_ins)
        console.run()
        if console.completed:
            print(f"Puzzle 2: accumulator value = {console.accumulator} (modified instruction {i})")
