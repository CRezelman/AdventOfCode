"""Day 17 Solve"""
import os
import sys
import re
from dataclasses import dataclass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines


@dataclass
class Computer:
    register_a: int
    register_b: int
    register_c: int
    program: list[int]
    output: list[int]

    def reset_output(self):
        self.output = []

    def output_str(self) -> str:
        return ",".join(map(str, self.output))
    
    def program_str(self) -> str:
        return ",".join(map(str, self.program))

    def combo(self, value: int) -> int:
        if value == 4:
            return self.register_a
        if value == 5:
            return self.register_b
        if value == 6:
            return self.register_c
        return value
        
    def simulate(self):
        instr_p = 0

        while instr_p < len(self.program):
            opcode = self.program[instr_p]
            operand = self.program[instr_p + 1]

            match opcode:
                case 0:
                    self.register_a >>= self.combo(operand)
                case 1:
                    self.register_b ^= operand
                case 2:
                    self.register_b = self.combo(operand) & 7
                case 3:
                    if self.register_a != 0:
                        instr_p = operand
                        continue
                case 4:
                    self.register_b ^= self.register_c
                case 5:
                    self.output.append(self.combo(operand) & 7)
                case 6:
                    self.register_b = self.register_a >> self.combo(operand)
                case 7:
                    self.register_c = self.register_a >> self.combo(operand)

            instr_p += 2

def run_single_step_output(A, program):
    rA = A
    rB = 0
    rC = 0
    ip = 0

    while True:
        opcode = program[ip]
        operand = program[ip + 1]

        # combo operand
        if operand == 4:
            cv = rA
        elif operand == 5:
            cv = rB
        elif operand == 6:
            cv = rC
        else:
            cv = operand

        match opcode:
            case 0:
                rA >>= cv

            case 1:
                rB ^= operand

            case 2:
                rB = cv & 7

            case 3:
                if rA != 0:
                    ip = operand
                    continue

            case 4:
                rB ^= rC

            case 5:
                # OUTPUT
                out = cv & 7
                return rA, out  # Note: rA already shifted earlier in instruction 0

            case 6:
                rB = rA >> cv

            case 7:
                rC = rA >> cv

        ip += 2

        
def reverse_search(program):
    """
    Given the full program output sequence, find all possible A values
    that produce EXACTLY that output list.
    Returns the smallest valid A.
    """
    target = program[:]  # desired output list
    target.reverse()

    # After the LAST output, A must be 0
    candidates = {0}

    for digit in target:
        new_set = set()

        for A_after in candidates:
            # A_before = (A_after << 3) | x   for x in 0..7
            for x in range(8):
                A_before = (A_after << 3) | x

                nextA, out = run_single_step_output(A_before, program)

                if out == digit and nextA == A_after:
                    new_set.add(A_before)

        candidates = new_set

        if not candidates:
            raise RuntimeError("No valid A found - inconsistent program")

    return min(candidates)

def parse_computer(lines: list[str]) -> Computer:
    lines = [line.strip() for line in lines if line.strip()]
    reg_a = int(lines[0].split(":")[1].strip())
    reg_b = int(lines[1].split(":")[1].strip())
    reg_c = int(lines[2].split(":")[1].strip())
    program_part = lines[3].split(":", 1)[1]
    program = [int(x) for x in program_part.split(",")]

    return Computer(register_a=reg_a, register_b=reg_b, register_c=reg_c, program=program, output=[])


def day17():
    """Day 17"""
    part1 = 0
    part2 = 0
    lines = read_lines(2024, 17)

    computer = parse_computer(lines)
    computer.simulate()
    part1 = computer.output_str()

    target_program = computer.program
    part2 = reverse_search(target_program)

    return part1, part2

print(day17())

