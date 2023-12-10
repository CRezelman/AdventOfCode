# 2023 Day 10 using BFS

from queue import Queue

def day10():
    part1 = 0
    part2 = 0

    with open('2023/inputs/day10.txt', 'r') as f:
        pipeMap = [line.strip() for line in f]

    MOVEMENT = {
        "|": [ ( 0, -1), ( 0, 1) ],
        "-": [ (-1,  0), ( 1, 0) ],
        "L": [ ( 0, -1), ( 1, 0) ],
        "J": [ ( 0, -1), (-1, 0) ],
        "7": [ (-1,  0), ( 0, 1) ],
        "F": [ ( 1,  0), ( 0, 1) ],
    }

    for yi, line in enumerate(pipeMap):
        for xi, char in enumerate(line):
            if char == 'S':
                x, y = xi, yi
                break

    q = Queue()
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        char = pipeMap[y + dy][x + dx]
        if char in MOVEMENT:
            for dx2, dy2 in MOVEMENT[char]:
                if x == x + dx + dx2 and y == y + dy + dy2:
                    q.put((1, (x + dx, y + dy)))

    dists = { (x,y): 0 }
    assert(q.qsize() == 2)

    while not q.empty():
        d, (x, y) = q.get()

        if (x, y) in dists:
            continue

        dists[(x, y)] = d

        for dx, dy in MOVEMENT[pipeMap[y][x]]:
            q.put((d + 1,(x + dx, y + dy)))

    part1 = max(dists.values())
    
    w = len(pipeMap[0])
    h = len(pipeMap)
    
    for y, line in enumerate(pipeMap):
        for x, char in enumerate(line):
            if (x, y) in dists:
                continue
            
            crosses = 0
            x2, y2 = x, y

            while x2 < w and y2 < h:
                char2 = pipeMap[y2][x2]
                if (x2, y2) in dists and char2 != "L" and char2 != "7":
                    crosses += 1
                x2 += 1
                y2 += 1


            if crosses % 2 == 1:
                part2 += 1


    return part1, part2

print(day10())
