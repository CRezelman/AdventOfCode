import itertools
import math

class Node:
    def __init__(self, id: str, left: str, right: str) -> None:
        self.id = id
        self.left = left
        self.right = right


def day8(): 
    part1 = 0
    part2 = 0
    nodes: list[Node] = []
    with open('2023/inputs/day8.txt', 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                instructions = line
            elif line != '':
                id, data = line.split(' = ')
                left, right = data.strip('()').split(', ')
                node = Node(id, left, right)
                nodes.append(node) 
    
    nextNode = next(node for node in nodes if node.id == 'AAA')

    for i, instruction in enumerate(itertools.cycle(instructions)):
        if instruction == 'L':
            nextNode =  next(node for node in nodes if node.id == nextNode.left)
        if instruction == 'R':
            nextNode =  next(node for node in nodes if node.id == nextNode.right)
        if nextNode.id == 'ZZZ':
            part1 = i + 1
            break
    
    nextNodes = [node for node in nodes if node.id.endswith('A')]
    results = []

    for nextNode in nextNodes:
        for i, instruction in enumerate(itertools.cycle(instructions)):
            if instruction == 'L':
                nextNode =  next(node for node in nodes if node.id == nextNode.left)
            if instruction == 'R':
                nextNode =  next(node for node in nodes if node.id == nextNode.right)
            if nextNode.id.endswith('Z'):
                results.append(i+1)
                break

    part2 = math.lcm(results[0], results[1], results[2], results[3], results[4], results[5])

    return part1, part2

print(day8())

