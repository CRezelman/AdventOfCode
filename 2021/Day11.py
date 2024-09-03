# import numpy as np


# def process_flash(map, flashes: set):
#     new_flashes = []
#     for i, row in enumerate(map):
#         for j, energy in enumerate(row):
#             if map[i][j] > 9 and (i, j) not in flashes:
#                 new_flashes.append((i, j))
#                 flashes.add((i, j))

#     if len(new_flashes) == 0:
#         return

#     for y, x in new_flashes:
#         top = y - 1 >= 0
#         bottom = y + 1 < len(map)
#         right = x + 1 < len(map[0])
#         left = x - 1 >= 0

#         if right:
#             map[y][x+1] += 1
#         if left:
#             map[y][x-1] += 1
#         if bottom:
#             map[y+1][x] += 1
#         if top:
#             map[y-1][x] += 1
#         if top and right:
#             map[y-1][x+1] += 1
#         if bottom and right:
#             map[y+1][x+1] += 1
#         if top and left:
#             map[y-1][x-1] += 1
#         if bottom and left:
#             map[y+1][x-1] += 1

#     return process_flash(map, flashes)



# def day11():
#     part1 = 0
#     part2 = 0
#     ITERATIONS_P1 = 100
#     ITERATIONS_P2 = 500

#     with open('2021/inputs/day11.txt') as f:
#         octopus_map = np.array([[int(char) for char in line.strip()] for line in f])

#     for k in range(ITERATIONS_P2):
#         octopus_map += 1

#         process_flash(octopus_map, set())
#         for i, row in enumerate(octopus_map):
#             for j, energy in enumerate(row):
#                 if octopus_map[i][j] > 9 :
#                     part1 += 1
#                     octopus_map[i][j] = 0
            
#         if np.all(octopus_map == 0) and part2 == 0:
#             part2 = k + 1

#     return part1, part2


# print(day11())

import numpy as np

def process_flash(octopus_map, flashes):
    while True:
        # Find all new flashes
        new_flashes = np.argwhere((octopus_map > 9) & (~flashes))
        
        if len(new_flashes) == 0:
            break

        flashes[tuple(new_flashes.T)] = True  # Mark these as flashed

        for y, x in new_flashes:
            # Determine the slice boundaries for surrounding cells
            y_min = max(y - 1, 0)
            y_max = min(y + 2, octopus_map.shape[0])
            x_min = max(x - 1, 0)
            x_max = min(x + 2, octopus_map.shape[1])

            # Increase energy levels of surrounding cells
            octopus_map[y_min:y_max, x_min:x_max] += 1

def day11():
    part1 = 0
    part2 = 0
    ITERATIONS_P1 = 100
    ITERATIONS_P2 = 500

    with open('2021/inputs/day11demo.txt') as f:
        octopus_map = np.array([[int(char) for char in line.strip()] for line in f])

    for k in range(ITERATIONS_P1):
        # Increase energy levels
        octopus_map += 1

        # Track flashes
        flashes = np.zeros_like(octopus_map, dtype=bool)
        process_flash(octopus_map, flashes)
        
        # Count flashes and reset energy levels
        part1 += np.sum(flashes)
        octopus_map[flashes] = 0

        # Check for synchronised flash
        if np.all(octopus_map == 0) and part2 == 0:
            part2 = k + 1

    return part1, part2

print(day11())
