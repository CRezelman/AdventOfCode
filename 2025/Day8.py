"""Day 8 Solve"""
from utilities.solver import Solver
import math
import itertools

class Day8(Solver):

    def calculate_distance(self, j1, j2):
        return math.sqrt(math.pow(abs(j1[0] - j2[0]), 2) + math.pow(abs(j1[1] - j2[1]), 2) + math.pow(abs(j1[2] - j2[2]), 2))

    def solve(self) -> None:
        self.junctions = set()
        for line in self.lines:
            self.junctions.add(tuple(int(x) for x in line.split(',')))

        distance_map = {}

        for j1, j2 in itertools.combinations(self.junctions, 2):
            if j1 == j2:
                continue
            distance = self.calculate_distance(j1, j2)
            distance_map[(j1, j2)] = distance

        distance_items = sorted(distance_map.items(), key=lambda x: x[1])

        self.circuits = [set([j]) for j in self.junctions]
        connections = 0
        MAX_CONNECTIONS = 1000
        for (j1, j2), distance in distance_items:
            if connections >= MAX_CONNECTIONS:
                break

            j1_circuit = next(circuit for circuit in self.circuits if j1 in circuit)
            j2_circuit = next(circuit for circuit in self.circuits if j2 in circuit)

            connections += 1
            if j1_circuit != j2_circuit:
                j1_circuit.update(j2_circuit)
                self.circuits.remove(j2_circuit)
                continue

        self.circuits.sort(key=lambda x: len(x), reverse=True)
        self.part1 = math.prod(len(circuit) for circuit in self.circuits[:3])

    
Day8(2025, 8).run()
