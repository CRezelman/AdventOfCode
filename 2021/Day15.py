"""Day 15"""
import numpy as np
import networkx as nx

def array_to_weighted_graph(grid) -> nx.DiGraph:
    """Convert 2D array to Weighted Directed Graph"""
    rows, cols = len(grid), len(grid[0])
    G = nx.DiGraph()

    for i in range(rows):
        for j in range(cols):
            G.add_node((i, j), weight=grid[i][j])

    for i in range(rows):
        for j in range(cols):
            if i > 0:
                G.add_edge((i, j), (i-1, j), weight=grid[i-1][j])
            if i < rows - 1:
                G.add_edge((i, j), (i+1, j), weight=grid[i+1][j])
            if j > 0:
                G.add_edge((i, j), (i, j-1), weight=grid[i][j-1])
            if j < cols - 1:
                G.add_edge((i, j), (i, j+1), weight=grid[i][j+1])

    return G

def expand_grid_numpy(original_grid):
    """Create 5x5 grid from orginal grid"""
    expanded_rows = []

    for i in range(5):
        row_grids = []

        for j in range(5):
            offset = i + j
            new_grid = (original_grid + offset - 1) % 9 + 1
            row_grids.append(new_grid)

        expanded_row = np.concatenate(row_grids, axis=1)
        expanded_rows.append(expanded_row)

    expanded_grid = np.concatenate(expanded_rows, axis=0)

    return expanded_grid


def day15():
    """Day 15"""
    part1 = 0
    part2 = 0
    with open('2021/inputs/day15.txt') as f:
        grid_p1 = np.array([[int(char) for char in line.strip()] for line in f])

    grid_p2 = expand_grid_numpy(grid_p1)

    G_P1 = array_to_weighted_graph(grid_p1)
    G_P2 = array_to_weighted_graph(grid_p2)

    # for edge in G.edges(data=True):
    #     print(edge)

    start_p1 = (0, 0)
    end_p1 = (len(grid_p1) - 1, len(grid_p1[0]) - 1)
    start_p2 = (0, 0)
    end_p2 = (len(grid_p2) - 1, len(grid_p2[0]) - 1)

    shortest_path_p1 = nx.dijkstra_path(G_P1, start_p1, end_p1, weight='weight')
    part1 = int(nx.dijkstra_path_length(G_P1, start_p1, end_p1, weight='weight'))

    shortest_path_p2 = nx.dijkstra_path(G_P2, start_p2, end_p2, weight='weight')
    part2 = int(nx.dijkstra_path_length(G_P2, start_p2, end_p2, weight='weight'))


    return part1, part2


print(day15())
