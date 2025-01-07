"""Day 2 Solve"""

def is_increasing(arr):
    """Is Array Increasing and each element differs by no more than 3"""
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1] or arr[i] - arr[i - 1] > 3:
            return False
    return True

def is_decreasing(arr):
    """Is Array Decreasing and each element differs by no more than 3"""
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1] or arr[i - 1] - arr[i] > 3:
            return False
    return True

def is_safe_p1(arr):
    """Is Array Increasing or Decreasing and each element differs by no more than 3"""
    return is_increasing(arr) or is_decreasing(arr)

def is_safe_p2(arr):
    """Returns True if the array is safe for part 1 or if we exclude 1 item from the array and is still safe for part 1."""
    for i in range(len(arr)):
        if is_safe_p1(arr[:i] + arr[i + 1:]):
            return True
    return False


def day2():
    """Day 2""" 
    part1 = 0
    part2 = 0
    data = open('2024/inputs/day2.txt', 'r', encoding='utf-8').read().strip().split('\n')

    reports = []

    for item in data:
        items = list(map(int, item.split(' ')))
        reports.append(items)

    for report in reports:
        if is_safe_p1(report):
            part1 += 1
            part2 += 1
        elif is_safe_p2(report):
            part2 += 1

    return part1, part2

print(day2())
