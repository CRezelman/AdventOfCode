"""Day 17"""
import re

def find_max_height(yf_min):
    """Uses sum of Natural Numbers to find max height"""
    return ((yf_min + 1) * yf_min) // 2


def distinct_velocitys(xf_min, xf_max, yf_min, yf_max):
    """Find Distinct Velocitys"""
    def hits_target(vx, vy):
        x = y = 0
        while True:
            # breaking conditions
            if x > xf_max: return False
            if vx == 0 and not xf_min <= x <= xf_max: return False
            if vx == 0 and y < yf_min: return False

            # target condition
            if xf_min <= x <= xf_max and yf_min <= y <= yf_max: return True

            x += vx
            y += vy

            if vx > 0: vx -= 1
            vy -= 1

    y_max = max(abs(yf_min), abs(yf_max))
    velocitys = 0

    for vx in range(xf_max + 1):
        for vy in range(-y_max, y_max + 1):
            velocitys += hits_target(vx, vy)

    return velocitys


def day17():
    """Day 17"""
    target_area = open('2021/inputs/day17.txt', 'r').read()
    x_match = re.search(r'x=(-?\d+)..(-?\d+)', target_area)
    y_match = re.search(r'y=(-?\d+)..(-?\d+)', target_area)
    xf_min, xf_max, yf_min, yf_max = int(x_match[1]), int(x_match[2]), int(y_match[1]), int(y_match[2])

    part1 = find_max_height(yf_min)
    part2 = distinct_velocitys(xf_min, xf_max, yf_min, yf_max)

    return (part1, part2)

print(day17())
