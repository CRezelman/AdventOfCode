class Rocks:
    def shape1(self):
        return [
            ['#', '#', '#', '#']
        ]

    def shape2(self):
        return [
            ['.', '#', '.'], 
            ['#', '#', '#'], 
            ['.', '#', '.']
        ]

    def shape3(self):
        return [
            ['.', '.', '#'], 
            ['.', '.', '#'], 
            ['#', '#', '#']
        ]

    def shape4(self):
        return [
            ['#'], 
            ['#'], 
            ['#'],
            ['#']
        ]

    def shape5(self):
        return [
            ['#', '#'], 
            ['#', '#']
        ]
    
    def getShapeByIndex(self, index: int):
        match ((index) % 5):
            case 0:
                return self.shape1()
            case 1:
                return self.shape2()
            case 2:
                return self.shape3()
            case 3:
                return self.shape4()
            case 4:
                return self.shape5()

    def moveShape(self, currentPosition, shape: list[list[str]], tunnel: list[list[str]], direction: str):
        # # Remove shape from tunnel
        # for i in range(len(shape)):
        #     for j in range(len(shape[i])):
        #         tunnel[currentPosition[0] + i][currentPosition[1] + j] = "."

        newPosition = currentPosition
        if direction == "v":
            if currentPosition[0] + len(shape) < len(tunnel) and self.canShapeMove(currentPosition, tunnel, shape, direction):
                newPosition = (currentPosition[0] + 1, currentPosition[1])
        elif direction == "<":
            if currentPosition[1] > 0 and self.canShapeMove(currentPosition, tunnel, shape, direction):
                newPosition = (currentPosition[0], currentPosition[1] - 1)
        elif direction == ">":
            if currentPosition[1] + len(shape[0]) < len(tunnel[0]) and self.canShapeMove(currentPosition, tunnel, shape, direction):
                newPosition = (currentPosition[0], currentPosition[1] + 1)

        # Add shape back to tunnel
        shape.reverse()
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                tunnel[newPosition[0] + i][newPosition[1] + j] = shape[i][j]
        shape.reverse()

        return newPosition
    
    
    def canShapeMove(self, currentPosition, tunnel: list[list[str]], shape: list[list[str]], direction: str):
        # Remove shape from tunnel
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                tunnel[currentPosition[0] + i][currentPosition[1] + j] = "."

        shapeHeight = len(shape)
        shapeWidth = len(shape[0])

        if direction == "<":
            new_position = (currentPosition[0], currentPosition[1] - 1)
        elif direction == ">":
            new_position = (currentPosition[0], currentPosition[1] + 1)
        elif direction == "v":
            new_position = (currentPosition[0] + 1, currentPosition[1])

        if (
            0 <= new_position[0] < len(tunnel) - shapeHeight + 1
            and 0 <= new_position[1] < len(tunnel[0]) - shapeWidth + 1
        ):
            # Check if each cell at the new position is '.'
            for i in range(shapeHeight):
                for j in range(shapeWidth):
                    if tunnel[new_position[0] + i][new_position[1] + j] != '.':
                        return False
            return True
        else:
            return False

    
    def canShapeMoveDown(self, tunnel: list[list[str]]) -> bool:
        canMoveDown = False
        for i, line in enumerate(tunnel):
            if (i+1) == len(tunnel): return False
            nextLine = tunnel[i + 1]
            if self.checkNoHashes(line, nextLine):
                canMoveDown = True
                break

        return canMoveDown
    

    def checkNoHashes(self, list1, list2):
        for char1, char2 in zip(list1, list2):
            if char1 == '#' and char2 == '#':
                return False
        return True
    


def insertShape(tunnel: list[list[str]], shape: list[list[str]]):
    for line in shape:
        tunnel.insert(0, ['.']*2 + line + ['.']*(5-len(line)))


def day17():
    currentPosition = (0, 0) # (y, x)
    tunnel = [['.' for i in range(7)] for j in range(3)]
    rocks = Rocks()
    shapeCounter = 0
    shape = Rocks.getShapeByIndex(rocks, shapeCounter)
    shape.reverse()
    with open('2022/inputs/day17demo.txt') as f:
        actions = f.read()
    actionIndex = 0

    insertShape(tunnel, shape)
    currentPosition = (0, 2)
    while shapeCounter < 2023:

        action = actions[actionIndex % len(actions)]
        currentPosition = Rocks.moveShape(rocks, currentPosition, shape, tunnel, action)


        if not Rocks.canShapeMove(rocks, currentPosition, tunnel, shape, 'v'):
        # if not Rocks.canShapeMoveDown(rocks, tunnel):
            # Add shape back to tunnel
            shape.reverse()
            for i in range(len(shape)):
                for j in range(len(shape[i])):
                    tunnel[currentPosition[0] + i][currentPosition[1] + j] = shape[i][j]
            shape.reverse()
            
            shapeCounter += 1
            shape = Rocks.getShapeByIndex(rocks, shapeCounter)
            shape.reverse()
            tunnel.insert(0, ['.', '.', '.', '.', '.', '.', '.'])
            tunnel.insert(0, ['.', '.', '.', '.', '.', '.', '.'])
            tunnel.insert(0, ['.', '.', '.', '.', '.', '.', '.'])
            tunnel.insert(0, ['.', '.', '.', '.', '.', '.', '.'])
            insertShape(tunnel, shape)
            currentPosition = (0, 2)

        currentPosition = Rocks.moveShape(rocks, currentPosition, shape, tunnel, 'v')
        if '#' not in tunnel[0]: 
            del tunnel[0]
            currentPosition = (currentPosition[0] - 1, currentPosition[1])
        actionIndex += 1


    print(tunnel)
    print(len(tunnel))


day17()