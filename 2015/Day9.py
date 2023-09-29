import itertools


def day9():
    locations = set()
    path = {}

    shortest = 999999
    longest = 0
    with open('2015/inputs/day9.txt') as f:
        for line in f:
            line = line.strip('\n')
            data = line.split(' ')

            city1 = data[0]
            city2 = data[2]
            distance = int(data[4])
            locations.add(city1)
            locations.add(city2)

            path[city1 + city2] = distance
            path[city2 + city1] = distance

    for route in itertools.permutations(locations):
        route_length = 0
        for city1, city2 in zip(route[:-1], route[1:]):
            route_length += path[city1 + city2]
        if route_length < shortest:
            shortest = route_length
        if route_length > longest:
            longest = route_length

    return shortest, longest


print(day9())
