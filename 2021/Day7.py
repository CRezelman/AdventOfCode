import math
import numpy as np

def day7():
    part1 = 0
    part2 = 0
    crabs = list[int]
    with open('2021/inputs/day7.txt') as f:
        crabs = [int(x) for x in f.readline().split(',')]

    median = np.median(crabs)
    mean = np.mean(crabs)

    for crab in crabs:
        moves1 = abs(crab - int(median))
        part1 += moves1
        for i in range(abs(crab - math.floor(mean))):
            part2 += (i+1)

    return part1, part2


print(day7())
