import math

class Roots:
    def __init__(self, a: int, b: int, c: int) -> None:
        d = (b**2) - (4*a*c)
        self.x1 = (-b - math.sqrt(d)) / (2*a)
        self.x2 = (-b + math.sqrt(d)) / (2*a)

    def integerDistance(self) -> int:
        return math.floor(max(self.x1, self.x2)) - math.ceil(min(self.x1, self.x2)) + 1


def day6(): 
    part1 = 1
    with open('2023/inputs/day6.txt', 'r') as file:
        lines = file.readlines()

    time = [int(value) for value in lines[0].split()[1::]]
    distance = [int(value) for value in lines[1].split()[1::]]
    races = list(zip(time, distance))

    for race in races:
        part1 *= Roots(-1, race[0], -race[1]).integerDistance()

    # y = -x^2 +58819679x - 434_104_122_218
    race = ( int(''.join(str(t[0]) for t in races)), int(''.join(str(t[1]) for t in races)) )
    part2 = Roots(-1, race[0], -race[1]).integerDistance()

    return part1, part2

print(day6())
