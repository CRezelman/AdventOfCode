"""Day 16 Solve"""
import os
import sys
import heapq
from collections import defaultdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_grid

DIRS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

DIR_ORDER = ["U", "R", "D", "L"]

def dijkstra_all_paths(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    # Min-dist table
    dist = {
        (r, c, d): float("inf")
        for r in range(rows)
        for c in range(cols)
        for d in DIR_ORDER
    }

    # Predecessors for path reconstruction
    parents = defaultdict(list)

    pq = []

    # Start facing right
    start_dir = "R"
    dist[(start[0], start[1], start_dir)] = 0
    heapq.heappush(pq, (0, start[0], start[1], start_dir))

    best_end_cost = float("inf")

    while pq:
        cost, r, c, d = heapq.heappop(pq)

        # Stop exploring worse states
        if cost > dist[(r, c, d)]:
            continue

        # Track the best cost to any "end in any direction"
        if (r, c) == end:
            if cost < best_end_cost:
                best_end_cost = cost
            continue

        # Explore all directions
        for nd in DIR_ORDER:
            dr, dc = DIRS[nd]
            nr, nc = r + dr, c + dc

            # Skip out of bounds
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            # Skip walls
            if maze[nr][nc] == "#":
                continue

            # Turning cost logic
            step_cost = 1 if nd == d else 1001
            new_cost = cost + step_cost

            # Update best cost
            if new_cost < dist[(nr, nc, nd)]:
                dist[(nr, nc, nd)] = new_cost
                parents[(nr, nc, nd)] = [(r, c, d)]
                heapq.heappush(pq, (new_cost, nr, nc, nd))

            # If equal cost, this is another optimal predecessor
            elif new_cost == dist[(nr, nc, nd)]:
                parents[(nr, nc, nd)].append((r, c, d))

    if best_end_cost == float("inf"):
        return None, [], set()

    # Collect all directions that reached the end with best cost
    end_states = [
        (end[0], end[1], d)
        for d in DIR_ORDER
        if dist[(end[0], end[1], d)] == best_end_cost
    ]

    # DFS to reconstruct all paths
    all_paths = []

    def build_paths(state, path):
        if state in parents:
            if len(parents[state]) == 0:
                all_paths.append(path[::-1])
                return
            for p in parents[state]:
                build_paths(p, path + [(p[0], p[1])])
        else:
            all_paths.append(path[::-1])

    for st in end_states:
        build_paths(st, [end])

    # Remove duplicates
    unique_paths = []
    seen = set()
    for p in all_paths:
        tup = tuple(p)
        if tup not in seen:
            seen.add(tup)
            unique_paths.append(p)

    # Collect unique coordinates across all optimal paths
    coord_set = set()
    for p in unique_paths:
        for cell in p:
            coord_set.add(cell)

    return best_end_cost, unique_paths, coord_set


def day16():
    """Day 16"""
    grid = read_grid(2024, 16).grid

    rows, cols = len(grid), len(grid[0])
    start = end = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)

    part1, all_paths, coords = dijkstra_all_paths(grid, start, end)
    part2 = len(coords)

    return part1, part2

print(day16())
