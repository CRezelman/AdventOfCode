import math

def day6(): 
    part1 = 1
    part2 = 1

    races = [(58, 434), (81, 1041), (96, 2219), (76, 1218)]

    for race in races:
        distances = []
        for t in range(race[0]):
            distance = t*(race[0] - t)
            if distance > race[1]:
                distances.append(distance)

        part1 = part1*len(distances)

    race = (58819676, 434_104_122_191_218)
    # y = -x^2 +58819679x - 434_104_122_218

    a = -1
    b = race[0]
    c = -race[1]

    d = (b**2) - (4*a*c)

    x1 = (-b-math.sqrt(d)/(2*a))
    x2 = (-b+math.sqrt(d)/(2*a))

    part2 = math.floor(abs(x2 - x1))


    return part1, part2

print(day6())
