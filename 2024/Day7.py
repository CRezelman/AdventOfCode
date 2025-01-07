"""Day 7 Solve"""
from dataclasses import dataclass
from utilities.input import read_lines

@dataclass
class Calibration:
    """Calibration"""
    result: int
    values: list[int]

def evaluate_expression(values: list[int], operations: list[str]) -> int:
    """Evaluate an expression from left to right"""
    result = values[0]
    for i in range(1, len(values)):
        if operations[i-1] == '+':
            result += values[i]
        elif operations[i-1] == '*':
            result *= values[i]
        elif operations[i-1] == '||':
            result = int(f"{result}{values[i]}")
    return result


def find_operations(values: list[int], target: int, operations: list[str]) -> bool:
    """Find Possible Operations"""
    def helper(index: int, current_ops: list[str]) -> bool:
        if index == len(values) - 1:
            result = evaluate_expression(values, current_ops)
            return result == target

        return any(helper(index + 1, current_ops + [op]) for op in operations)


    return helper(0, [])


def day7():
    """Day 7""" 
    part1 = 0
    part2 = 0
    lines = read_lines(2024, 7)
    calibrations: list[Calibration] = []
    operations_p1 = ['+', '*']
    operations_p2 = ['+', '*', '||']


    for line in lines:
        result, values = line.split(': ')
        values = values.split(' ')
        calibrations.append(Calibration(result=int(result), values=[int(value) for value in values]))

    for calibration in calibrations:
        if find_operations(calibration.values, calibration.result, operations_p1):
            part1 += calibration.result
        if find_operations(calibration.values, calibration.result, operations_p2):
            part2 += calibration.result


    return part1, part2

print(day7())
