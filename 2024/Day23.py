"""Day 23 Solve"""
import sys
import os
from itertools import combinations
import networkx as nx
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines

def find_triangles(G: nx.Graph):
    triangles = set()

    for u in G.nodes():
        for v in G.neighbors(u):
            if v <= u:
                continue
            common = set(G.neighbors(u)).intersection(G.neighbors(v))
            for w in common:
                if w <= v:
                    continue
                triangles.add(tuple(sorted([u, v, w])))

    return list(triangles)

def largest_interconnected_set_exact(G):
    cliques = list(nx.find_cliques(G))
    max_size = max(len(c) for c in cliques)
    largest = [c for c in cliques if len(c) == max_size]
    return largest[0]

def day23():
    """Day 23"""
    part1 = 0
    part2 = 0
    lines = read_lines(2024, 23)

    G = nx.Graph()

    for line in lines:
        left, right = line.strip().split("-")
        G.add_node(left)
        G.add_node(right)
        G.add_edge(left, right)

    triangles = find_triangles(G)

    for (a, b, c) in triangles:
        if any([a.startswith('t'), b.startswith('t'), c.startswith('t')]):
            part1 += 1

    largest_sets = largest_interconnected_set_exact(G)
    part2 = ','.join(sorted(largest_sets))

    return part1, part2

print(day23())
