"""Day 9 Solve"""
from utilities.input import read_lines

def re_order_file_system_p1(lst: list[int | None]):
    """Re-order list for part 1"""
    end_index = len(lst) - 1

    for i, _ in enumerate(lst):
        if lst[i] is None:
            while end_index > i and lst[end_index] is None:
                end_index -= 1

            if end_index > i:
                lst[i], lst[end_index] = lst[end_index], None
                end_index -= 1

    return lst

def re_order_file_system_p2(lst: list[int | None]):
    """Re-order list for part 2"""
    groups = []
    i = len(lst) - 1
    while i >= 0:
        if lst[i] is not None:
            group = []
            value = lst[i]
            while i >= 0 and lst[i] == value:
                group.append(value)
                i -= 1
            groups.append((value, len(group), i + 1))
        else:
            i -= 1

    for value, group_size, original_start in groups:
        for i in range(original_start + 1):
            if all(x is None for x in lst[i:i + group_size]):
                lst[i:i + group_size] = [value] * group_size
                lst[original_start:original_start + group_size] = [None] * group_size
                break

    return lst


def calculate_checksum(lst: list[int | None]):
    """Calculate Checksum value"""
    result = 0
    for index, value in enumerate(lst):
        if value is not None:
            result += value * index
    return result

def day9():
    """Day 9"""
    part1 = 0
    part2 = 0
    data = read_lines(2024, 9)[0]
    file_system: list[int | None] = []

    for count, value in enumerate(data):
        if count % 2 == 0:
            for _ in range(int(value)):
                file_system.append(int(count) // 2)
        else:
            for _ in range(int(value)):
                file_system.append(None)

    file_system_p1 = re_order_file_system_p1(file_system.copy())
    file_system_p2 = re_order_file_system_p2(file_system.copy())

    part1 = calculate_checksum(file_system_p1)
    part2 = calculate_checksum(file_system_p2)

    return part1, part2

print(day9())
