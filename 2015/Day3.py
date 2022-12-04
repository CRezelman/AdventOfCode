def day3():
    x = 0 
    y = 0
    houses = [[0, 0]]

    santaX = 0
    santaY = 0
    roboX = 0
    roboY = 0
    houses2 = [[0, 0]]
    with open('2015/day3.txt') as f:
        for index, char in enumerate(f.readline()):
            if char == '>':
                x += 1
            elif char == '<':
                x -= 1
            elif char == '^':
                y += 1
            elif char == 'v':
                y -= 1
            
            if [x, y] not in houses:
                houses.append([x, y])

            if index % 2 == 0:
                if char == '>':
                    santaX += 1
                elif char == '<':
                    santaX -= 1
                elif char == '^':
                    santaY += 1
                elif char == 'v':
                    santaY -= 1

                if [santaX, santaY] not in houses2:
                    houses2.append([santaX, santaY])
            
            if index % 2 == 1:
                if char == '>':
                    roboX += 1
                elif char == '<':
                    roboX -= 1
                elif char == '^':
                    roboY += 1
                elif char == 'v':
                    roboY -= 1

                if [roboX, roboY] not in houses2:
                    houses2.append([roboX, roboY])
        
    return len(houses), len(houses2)


print(day3())