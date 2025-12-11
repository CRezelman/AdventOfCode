"""Day 11 Solve"""
from utilities.solver import Solver
import networkx as nx

class Day11(Solver):
    def solve(self) -> None:
        G = nx.DiGraph()
        for line in self.lines:
            input, output = line.split(': ')
            output = output.split(' ')
            G.add_node(input)
            for out in output:
                G.add_edge(input, out)

        self.part1 = len(list(nx.all_simple_paths(G, source='you', target='out')))
    
Day11(2025, 11).run()
