from itertools import combinations

class Hail:
    def __init__(self, px, py, pz, vx, vy, vz, id) -> None:
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.id = id
        pass

    @property
    def m(self) -> int:
        return self.vy / self.vx

    @property
    def c(self) -> int:
        return self.py - self.m * self.px
    

def findIntersection(hail1: Hail, hail2: Hail):
    if hail1.m == hail2.m: return None, None

    resX = (hail2.c - hail1.c) / (hail1.m - hail2.m)
    resY = hail1.m * resX + hail1.c
    return (resX, resY)


def day24():
    part2 = 0
    part1 = 0
    hails: list[Hail] = []
    low =  200000000000000
    high = 400000000000000

    for i, line in enumerate(open('2023/inputs/day24.txt', 'r').read().splitlines()):
        positions, velocities = line.strip().split(' @ ')
        px, py, pz = list(map(int, positions.split(', ')))
        vx, vy, vz = list(map(int, velocities.split(', ')))
        hails.append(Hail(px, py, pz, vx, vy, vz, i+1))

    for hail1, hail2 in combinations(hails, 2):
        x, y = findIntersection(hail1, hail2)
        if x == None or y == None: continue

        if  (hail1.px < x and hail1.vx < 0) or \
            (hail2.px < x and hail2.vx < 0) or \
            (hail1.px > x and hail1.vx > 0) or \
            (hail2.px > x and hail2.vx > 0):
            continue

        if low <= x <= high and low <= y <= high:
            part1 += 1


    return part1, part2

print(day24())