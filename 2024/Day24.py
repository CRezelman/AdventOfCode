"""Day 24 Solve"""
import sys
import os
from dataclasses import dataclass
from typing import Literal
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines

@dataclass
class Instruction:
    input1: str
    input2: str
    op: Literal['AND', 'OR', 'XOR']
    output: str


def parse_data(lines: list[str]) -> tuple[dict[str, bool], dict[str, Instruction]]:
    values = {}
    gates = {}

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
        gates[out] = Instruction(p1, p2, op, out)
        i += 1

    return values, gates


def evaluate_wire(wire: str, values: dict[str, bool], gates: dict[str, Instruction], cache: dict[str, bool]) -> bool:
    if wire in cache:
        return cache[wire]

    if wire in values:
        cache[wire] = values[wire]
        return values[wire]
    instr = gates[wire]

    left = evaluate_wire(instr.input1, values, gates, cache)
    right = evaluate_wire(instr.input2, values, gates, cache)

    match instr.op:
        case "AND":
            result = left and right
        case "OR":
            result = left or right
        case "XOR":
            result = (left != right)
    cache[wire] = result
    return result


def day24():
    """Day 24"""
    part1 = 0
    part2 = 0

    lines = read_lines(2024, 24)
    values, gates = parse_data(lines)

    cache = {}

    for wire in gates:
        if evaluate_wire(wire, values, gates, cache):
            if wire.startswith("z"):
                bit_index = int(wire[1:])
                part1 += (1 << bit_index)

    return part1, part2


print(day24())
