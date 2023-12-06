import math

def findRoots(a: int, b: int, c: int) -> tuple[int, int]:
    d = (b**2) - (4*a*c)
    x1 = (-b - math.sqrt(d)) / (2*a)
    x2 = (-b + math.sqrt(d)) / (2*a)
    return (x1, x2)


def day6(): 
    part1 = 1
    races = [(58, 434), (81, 1041), (96, 2219), (76, 1218)]

    for race in races:
        x1, x2 = findRoots(-1, race[0], -race[1])
        part1 *= math.floor(max(x1, x2)) - math.ceil(min(x1, x2)) + 1


    race = (58819676, 434_104_122_191_218)
    # y = -x^2 +58819679x - 434_104_122_218

    x1, x2 = findRoots(-1, race[0], -race[1])
    part2 = math.floor(max(x1, x2)) - math.ceil(min(x1, x2)) + 1


    return part1, part2

print(day6())
