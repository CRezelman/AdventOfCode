import networkx as nx
import random

def day25():
    graph = nx.Graph()

    for line in open('2023/inputs/day25.txt', 'r').read().splitlines():
        source, destinations = line.strip().split(': ')
        destinations = destinations.split(' ')
        for dest in destinations:
            graph.add_edge(source, dest, capacity=1)

    while True:
        nodes = list(graph.nodes())
        a, b = random.choices(nodes, k=2)
        if a == b:
            continue
        cut, partition = nx.minimum_cut(graph, a, b)
        if cut == 3:
            return len(partition[0]) * len(partition[1])

print(day25())