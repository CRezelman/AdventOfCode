
class Node():
    x = 0
    y = 0

    def __init__(self, x, y):
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


def day9(knots):
    locations = 0

    nodes = []

    for i in range(knots):
        nodes.append(Node(0,0))

    tailPlaces = set()

    with open('2022/inputs/day9.txt') as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            dir, count = line.split(' ')

            for j in range(int(count)):
                if dir == 'R':
                    nodes[0].x += 1

                elif dir == 'L':
                    nodes[0].x -= 1

                elif dir == 'U':
                    nodes[0].y += 1

                elif dir == 'D':
                    nodes[0].y -= 1

                for j in range(len(nodes)-1):
                    if checkDist(nodes[j], nodes[j+1]):
                        updateNode(nodes[j], nodes[j+1])
                
                tailPlaces.add((nodes[len(nodes)-1].x, nodes[len(nodes)-1].y))

        locations = len(tailPlaces)

    return locations

print(day9(2))
print(day9(10))