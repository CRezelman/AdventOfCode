"""Day 12"""
import networkx as nx
import pylab as p

def find_all_paths(G, start, end, path=[], visited=None):
    """DFS"""
    if visited is None:
        visited = {node: 0 for node in G.nodes()}

    path = path + [start]
    if start == end:
        return [path]
    
    if start.islower():
        visited[start] += 1

    paths = []
    for node in G.neighbors(start):
        if node.isupper() or visited[node] == 0:
            new_paths = find_all_paths(G, node, end, path, visited.copy())
            for new_path in new_paths:
                paths.append(new_path)
    
    return paths


def find_all_paths_with_one_twice(G, start, end, can_visit_twice, path=[], visited=None):
    if visited is None:
        visited = {node: 0 for node in G.nodes()}

    path = path + [start]
    if start == end:
        return [path]

    if start.islower():
        visited[start] += 1

    paths = []
    for node in G.neighbors(start):
        if node == can_visit_twice and visited[node] < 2:
            new_paths = find_all_paths_with_one_twice(G, node, end, can_visit_twice, path, visited.copy())
            for new_path in new_paths:
                paths.append(new_path)
        elif node.isupper() or visited[node] == 0:
            new_paths = find_all_paths_with_one_twice(G, node, end, can_visit_twice, path, visited.copy())
            for new_path in new_paths:
                paths.append(new_path)
    
    return paths


def get_all_unique_paths(G, start, end):
    all_paths = set()

    lowercase_nodes = [node for node in G.nodes() if node.islower() and node not in {'start', 'end'}]

    for node in lowercase_nodes:
        paths = find_all_paths_with_one_twice(G, start, end, can_visit_twice=node)
        for path in paths:
            all_paths.add(tuple(path))

    return sorted(list(all_paths))


def day12():
    """Day 12"""
    part1 = 0
    part2 = 0
    G = nx.Graph()

    for line in open('2021/inputs/day12.txt', 'r').read().splitlines():
        source, destination = line.strip().split('-')
        G.add_edge(source, destination)

    all_paths = find_all_paths(G, 'start', 'end')
    part1 = len(all_paths)

    unique_paths = get_all_unique_paths(G, 'start', 'end')
    part2 = len(unique_paths)

    # nx.draw(G, with_labels=True)
    # p.show()
    return part1, part2

print(day12())
