"""Day 1 Solve"""
from collections import Counter

def day1():
    """Day 1""" 
    part1 = 0
    part2 = 0
    data = open('2024/inputs/day1.txt', 'r', encoding='utf-8').read().strip().split('\n')
    left = []
    right = []

    for item in data:
        item = item.split('   ')
        left.append(int(item[0]))
        right.append(int(item[1]))

    left.sort()
    right.sort()

    right_counter = dict(Counter(right))


    for l, r in zip(left, right):
        part1 += abs(l - r)

    for item in left:
        part2 += right_counter.get(item, 0) * item

    return part1, part2

print(day1())
