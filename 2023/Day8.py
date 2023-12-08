import itertools
import math

class Node:
    def __init__(self, id: str, left: str, right: str) -> None:
        self.id = id
        self.left = left
        self.right = right


def findResult(instructions: str, condition: str,  nodes: list[Node], nextNode: Node) -> int:
    for i, instruction in enumerate(itertools.cycle(instructions)):
        nextNode =  next(node for node in nodes if node.id == (nextNode.left if instruction == 'L' else nextNode.right))
        if nextNode.id.endswith(condition):
            return i + 1
    

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
    part1 = findResult(instructions, 'ZZZ', nodes, nextNode)
    
    nextNodes = [node for node in nodes if node.id.endswith('A')]
    results = []

    for nextNode in nextNodes:
        results.append(findResult(instructions, 'Z', nodes, nextNode))

    part2 = math.lcm(*results)

    return part1, part2

print(day8())

