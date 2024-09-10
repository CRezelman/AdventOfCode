"""Day 18"""
import math
import ast
import copy

class SnailfishNumber:
    """Snailfish Number"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def is_regular_number(self, value):
        """ Helper to check if the value is a regular number. """
        return isinstance(value, int)

    def explode(self, depth=0):
        """ Explode if this pair is at depth 4 or more. Returns explosion info. """
        if depth == 4:
            return self.left, self.right, 0
        if isinstance(self.left, SnailfishNumber):
            left_exploded = self.left.explode(depth + 1)
            if left_exploded is not None:
                left_val, right_val, new_left = left_exploded
                self.left = new_left
                if right_val is not None:
                    if self.is_regular_number(self.right):
                        self.right += right_val
                        right_val = None
                    else:
                        self.right.add_to_leftmost(right_val)
                        right_val = None
                return left_val, right_val, self
        if isinstance(self.right, SnailfishNumber):
            right_exploded = self.right.explode(depth + 1)
            if right_exploded is not None:
                left_val, right_val, new_right = right_exploded
                self.right = new_right
                if left_val is not None:
                    if self.is_regular_number(self.left):
                        self.left += left_val
                        left_val = None
                    else:
                        self.left.add_to_rightmost(left_val)
                        left_val = None
                return left_val, right_val, self
        return None

    def add_to_leftmost(self, value):
        """ Add value to the leftmost regular number. """
        if self.is_regular_number(self.left):
            self.left += value
        else:
            self.left.add_to_leftmost(value)

    def add_to_rightmost(self, value):
        """ Add value to the rightmost regular number. """
        if self.is_regular_number(self.right):
            self.right += value
        else:
            self.right.add_to_rightmost(value)

    def split(self):
        """ Split a regular number if >= 10. """
        if self.is_regular_number(self.left) and self.left >= 10:
            self.left = SnailfishNumber(self.left // 2, math.ceil(self.left / 2))
            return True
        if isinstance(self.left, SnailfishNumber) and self.left.split():
            return True
        if self.is_regular_number(self.right) and self.right >= 10:
            self.right = SnailfishNumber(self.right // 2, math.ceil(self.right / 2))
            return True
        if isinstance(self.right, SnailfishNumber) and self.right.split():
            return True
        return False

    def reduce(self):
        """ Reduce the number by exploding and splitting until no more reductions can be done. """
        while True:
            exploded = self.explode()
            if exploded:
                continue
            if self.split():
                continue
            break
        return self

    def magnitude(self):
        """ Recursively calculate the magnitude of the snailfish number. """
        left_magnitude = self.left if self.is_regular_number(self.left) else self.left.magnitude()
        right_magnitude = self.right if self.is_regular_number(self.right) else self.right.magnitude()
        return 3 * left_magnitude + 2 * right_magnitude

    @staticmethod
    def add(sn1, sn2):
        """ Add two snailfish numbers and reduce the result. """
        return SnailfishNumber(sn1, sn2).reduce()

    def __repr__(self):
        return f"[{self.left}, {self.right}]"

def parse_input(data):
    """ Parse the input data to create SnailfishNumber objects. """
    def parse_number(item):
        if isinstance(item, int):
            return item
        return SnailfishNumber(parse_number(item[0]), parse_number(item[1]))

    return [parse_number(ast.literal_eval(line)) for line in data.splitlines()]


def day18():
    """Day 18 Solve"""
    input_data = open('2021/inputs/day18.txt', 'r', encoding='utf-8').read()
    numbers = parse_input(input_data)
    copy_numbers = copy.deepcopy(numbers)

    result = copy_numbers[0]
    for num in copy_numbers[1:]:
        result = SnailfishNumber.add(result, num)

    part1 = result.magnitude()
    part2 = 0
    for i, _ in enumerate(numbers):
        for j, _ in enumerate(numbers):
            if i != j:
                sum_result = SnailfishNumber.add(copy.deepcopy(numbers[i]), copy.deepcopy(numbers[j])).magnitude()
                part2 = max(part2, sum_result)

    return (part1, part2)

print(day18())
