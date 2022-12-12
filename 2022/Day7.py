
class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.size = 0
        self.child = []

    def addNode(self, key, parent):
        self.child.append(Node(key, parent))

    def __repr__(self):
        return repr(vars(self))

    def __str__(self) -> str:
        return str(self.__dict__)

def checkSize(node: Node, spaceReq, possibleNodes):
    for child in node.child:
        if child.size >= spaceReq and len(child.child) != 0:
            possibleNodes.append(child.size)
            checkSize(child, spaceReq, possibleNodes)

# def size(node, sizes):
#     for child in node.child:
#         if len(child.child) != 0:
#             sizes.append(child.size)


def day7():
    part1 = 0
    part2 = 0
    currentDir = ''
    depth = 0
    with open('2022/inputs/day7.txt') as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            if '$ cd /' in line:
                root = Node(line.split(' ')[2], 0)
                currentDir = root

            elif 'dir' in line:
                currentDir.addNode(line.split(' ')[1], currentDir)

            elif '$ cd' in line:
                newDir = line.split(' ')[2]
                if newDir == '..':
                    depth -= 1
                    if currentDir.size <= 100000:
                        part1 += currentDir.size
                    if depth == 0:
                        currentDir = root
                    else:
                        currentDir.parent.size += currentDir.size
                        currentDir = currentDir.parent
                    

                else:
                    depth += 1
                    for child in currentDir.child:
                        if child.key == newDir:
                            currentDir = child

            elif '$' not in line and 'dir' not in line:
                currentDir.addNode(line.split(' ')[1], currentDir)
                for child in currentDir.child:
                    if child.key == line.split(' ')[1]:
                        child.size = int(line.split(' ')[0])
                currentDir.size += int(line.split(' ')[0])

    root.size = 0
    for child in root.child:
        root.size += child.size

    spaceRequired = root.size - 40000000
    print(spaceRequired)

    # part2 = checkSize(root, spaceRequired)
    possibleNodes = []
    possibleNodes.append(root.size)
    checkSize(root, spaceRequired, possibleNodes)
    part2 = min(possibleNodes)


    # print(root.size)
    # print(root)

    return part1, part2

print(day7())

