"""Day 8 Solve"""
from utilities.solver import Solver
import math
import itertools

class Day8(Solver):
    def solve(self) -> None:
        self.junctions = {tuple(int(x) for x in line.split(',')) for line in self.lines}
        self.circuits = [set([j]) for j in self.junctions]

        self.distance_map = {(j1, j2): math.dist(j1, j2) for j1, j2 in itertools.combinations(self.junctions, 2)}
        self.distance_map = sorted(self.distance_map.items(), key=lambda x: x[1])

        for i, ((j1, j2), _) in enumerate(self.distance_map):
            if i == 1000:
                self.circuits.sort(key=lambda x: len(x), reverse=True)
                self.part1 = math.prod(len(circuit) for circuit in self.circuits[:3])

            j1_circuit = next(circuit for circuit in self.circuits if j1 in circuit)
            j2_circuit = next(circuit for circuit in self.circuits if j2 in circuit)

            if j1_circuit != j2_circuit:
                j1_circuit.update(j2_circuit)
                self.circuits.remove(j2_circuit)
                if len(self.circuits) == 1:
                    self.part2 = j1[0] *j2[0]
                    break
                continue
    
Day8(2025, 8).run()
