
class Node():
    x = 0
    y = 0

    def __init__(self, x, y, prevX, prevY):
        self.x = x
        self.y = y


def checkDist(node1: Node, node2: Node):
    return abs(node1.x - node2.x) >= 2 or abs(node1.y - node2.y) >= 2

def updateNode(node1: Node, node2: Node):
    if node1.x > node2.x:
        node2.x += 1
    if node1.x < node2.x:
        node2.x -= 1
    if node1.y > node2.y:
        node2.y += 1
    if node1.y < node2.y:
        node2.y -= 1


def day9_2():
    part1 = 0
    part2 = 0

    head = Node(0,0,0,0)
    node2 = Node(0,0,0,0)
    node3 = Node(0,0,0,0)
    node4 = Node(0,0,0,0)
    node5 = Node(0,0,0,0)
    node6 = Node(0,0,0,0)
    node7 = Node(0,0,0,0)
    node8 = Node(0,0,0,0)
    node9 = Node(0,0,0,0)
    tail = Node(0,0,0,0)

    tailPlaces = set()

    with open('2022/inputs/day9.txt') as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            dir, count = line.split(' ')

            for j in range(int(count)):
                if dir == 'R':
                    head.x +=1

                elif dir == 'L':
                    head.x -= 1

                elif dir == 'U':
                    head.y += 1

                elif dir == 'D':
                    head.y -= 1

                ## Part 1 ##
                # if checkDist(head, tail):
                #     updateNode(head, tail)

                if checkDist(head, node2):
                    updateNode(head, node2)

                if checkDist(node2, node3):
                    updateNode(node2, node3)

                if checkDist(node3, node4):
                    updateNode(node3, node4)

                if checkDist(node4, node5):
                    updateNode(node4, node5)

                if checkDist(node5, node6):
                    updateNode(node5, node6)

                if checkDist(node6, node7):
                    updateNode(node6, node7)

                if checkDist(node7, node8):
                    updateNode(node7, node8)

                if checkDist(node8, node9):
                    updateNode(node8, node9)

                if checkDist(node9, tail):
                    updateNode(node9, tail)

                tailPlaces.add((tail.x, tail.y))
        part1 = len(tailPlaces)

    return part1, part2

print(day9_2())