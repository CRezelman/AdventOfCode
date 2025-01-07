"""Day 6 Solve"""
from utilities.input import read_grid
from utilities.grid import search_grid


def day6():
    """Day 6""" 
    part1 = 0
    part2 = 0
    grid = read_grid(2024, 6, False)
    current_pos = (0, 0)
    current_dir = (-1, 0)
    obstacles = []
    visited_p1 = set()

    def update_start_pos(y, x):
        nonlocal current_pos
        current_pos = (y, x)
        visited_p1.add((y, x))

    def update_obstacles(y, x):
        nonlocal obstacles
        obstacles.append((y, x))

    search_grid(grid=grid, condition='^', callback=update_start_pos)
    search_grid(grid=grid, condition='#', callback=update_obstacles)


    def will_cause_infinite_loop(grid, start_pos, start_dir):
        current_pos = start_pos
        current_dir = start_dir
        visited = set()

        while True:
            next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])
            if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[0]):
                return False

            if (next_pos, current_dir) in visited:
                return True

            visited.add((next_pos, current_dir))

            if grid[next_pos[0]][next_pos[1]] == '#':
                current_dir = (current_dir[1], -current_dir[0])
                continue

            current_pos = next_pos

    def check_infinite_loop(y, x):
        nonlocal grid, part2
        grid[y][x] = '#'
        if will_cause_infinite_loop(grid, current_pos, current_dir):
            part2 += 1
        grid[y][x] = '.'


    search_grid(grid=grid, condition='.', callback=check_infinite_loop)

    while True:
        next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])
        if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[0]):
            break

        if grid[next_pos[0]][next_pos[1]] == '#':
            current_dir = (current_dir[1], -current_dir[0])
            continue

        visited_p1.add(next_pos)
        current_pos = next_pos

    part1 = len(visited_p1)


    return part1, part2

print(day6())
