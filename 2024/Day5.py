"""Day 5 Solve"""
from dataclasses import dataclass
from utilities.input import read_lines

@dataclass
class Rule:
    """Page Ordering Rules"""
    start: int
    end: int

def update_passes_rule(rule: Rule, update: list[int]) -> bool:
    """
    Check if the update passes the rule. 
    Start of rule must appear before the end of the rule in the update. 
    If rule is not present in update, it passes.
    """
    if rule.start not in update or rule.end not in update:
        return True
    return update.index(rule.start) < update.index(rule.end)


def find_middle_item(lst):
    """Find the item in the middle of the list."""
    if not lst:
        return None
    middle_index = len(lst) // 2
    return lst[middle_index]


def swap_elements(lst, index1, index2):
    """Swap elements at index1 and index2 in the list"""
    lst[index1], lst[index2] = lst[index2], lst[index1]


def day5():
    """Day 5""" 
    part1 = 0
    part2 = 0
    data: list[str] = read_lines(2024, 5, False)

    new_line_found = False
    rules: list[Rule] = []
    updates: list[list[int]] = []

    for line in data:
        if line == '':
            new_line_found = True
            continue
        if not new_line_found:
            start, end = line.split('|')
            rules.append(Rule(int(start), int(end)))
        if new_line_found:
            updates.append([int(x) for x in line.split(',')])

    for update in updates:
        if all(update_passes_rule(rule, update) for rule in rules):
            part1 += find_middle_item(update)
        else:
            while not all(update_passes_rule(rule, update) for rule in rules):
                for rule in rules:
                    if not update_passes_rule(rule, update):
                        swap_elements(update, update.index(rule.start), update.index(rule.end))
            part2 += find_middle_item(update)


    return part1, part2

print(day5())
