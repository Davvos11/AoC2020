import re
import time
from typing import Dict

programType = (str, int, int) or (str, str)


def read_line(line: str) -> programType:
    action, value = re.findall(r"(.+) = (.+)", line)[0]
    if action.startswith('mem'):
        action, value1, value2 = re.findall(r"(\w+)\[(\d+)] = (\d+)", line)[0]
        return action, int(value1), int(value2)
    else:
        return action, value


def read_input(filename: str):
    with open(filename) as file:
        return [read_line(line.strip()) for line in file]


class Program:
    def __init__(self, program: programType, val_length=36):
        self.program = program
        self.val_length = val_length
        self.mask = "X" * val_length
        self.memory: Dict[int, int] = dict()

    def init(self):
        for instruction in self.program:
            if instruction[0] == 'mask':
                self.mask = instruction[1]
            elif instruction[0] == 'mem':
                self.set_memory(instruction[1], instruction[2])
            else:
                print(f"Unsupported instruction: {instruction}")

    def set_memory(self, address: int, value: int):
        # Convert value to bits
        bits = self.int_to_bits(value)
        # Apply mask
        bits = self.apply_mask(bits)
        # Convert back to integer and update memory
        self.memory[address] = self.bits_to_int(bits)

    def apply_mask(self, bits: [int]):
        for i, mask_bit in enumerate(self.mask):
            if mask_bit != 'X':
                bits[i] = int(mask_bit)
        return bits

    def int_to_bits(self, value: int) -> [int]:
        bits = [1 if digit == '1' else 0 for digit in bin(value)[2:]]
        # Zero pad
        while len(bits) < self.val_length:
            bits.insert(0, 0)
        return bits

    @staticmethod
    def bits_to_int(bits: [int]) -> int:
        value = 0
        for bit in bits:
            value = value * 2 + bit
        return value


class Program2(Program):

    def set_memory(self, address: int, value: int):
        # Convert address to bits
        bits = self.int_to_bits(address)
        # Apply mask
        addresses = self.apply_address_mask(bits)
        # Update those memory location
        for address in addresses:
            self.memory[address] = value

    def apply_address_mask(self, bits: [int]) -> [int]:
        addresses = [[]]
        for i, mask_bit in enumerate(self.mask):
            if mask_bit == '1':
                for a in addresses:
                    a.append(1)
            elif mask_bit == '0':
                for a in addresses:
                    a.append(bits[i])
            elif mask_bit == 'X':
                new_addresses = []
                for a in addresses:
                    b = a.copy()
                    a.append(0)
                    b.append(1)
                    new_addresses.append(b)
                addresses += new_addresses

        return [self.bits_to_int(a) for a in addresses]


if __name__ == '__main__':
    input14 = read_input('input/day14')

    t1 = time.time()
    program = Program(input14)
    program.init()
    print(f"Part 1: sum of memory: {sum(program.memory.values())}")
    print(f"   Time: {(time.time() - t1) * 1000} ms")

    t1 = time.time()
    program = Program2(input14)
    program.init()
    print(f"Part 2: sum of memory: {sum(program.memory.values())}")
    print(f"   Time: {(time.time() - t1) * 1000} ms")
