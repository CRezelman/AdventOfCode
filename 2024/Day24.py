"""Day 24 Solve"""
import sys
import os
from dataclasses import dataclass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines

@dataclass
class Instruction:
    input1: str
    input2: str
    op: str
    output: str


def parse_data(lines) -> tuple[dict[str, bool], list[Instruction]]:
    values = {}
    instructions = []

    i = 0
    while i < len(lines) and lines[i].strip():
        key, val = lines[i].split(":")
        values[key.strip()] = (val.strip() == "1")
        i += 1

    while i < len(lines) and not lines[i].strip():
        i += 1

    while i < len(lines) and lines[i].strip():
        left, out = lines[i].split("->")
        out = out.strip()
        p1, op, p2 = left.strip().split()

        instructions.append(
            Instruction(input1=p1, input2=p2, op=op, output=out)
        )

        i += 1

    return values, instructions



def day24():
    """Day 24"""
    part1 = 0
    part2 = 0
    lines = read_lines(2024, 24)
    values, instructions = parse_data(lines)

    while len(instructions):
       for instr in instructions:
           if instr.input1 in values and instr.input2 in values:
               if instr.op == "AND":
                   values[instr.output] = values[instr.input1] and values[instr.input2]
               elif instr.op == "OR":
                   values[instr.output] = values[instr.input1] or values[instr.input2]
               elif instr.op == "XOR":
                   values[instr.output] = values[instr.input1] != values[instr.input2]

               instructions.remove(instr)
               break 
           
    values = dict(sorted(values.items(), reverse=True))
    binary_str = ''.join(['1' if values[key] else '0' for key in values.keys() if key.startswith("z")])
    part1 = int(binary_str, 2)

    return part1, part2

print(day24())
