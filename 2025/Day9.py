"""Day 9 Solve"""
from utilities.solver import Solver
from itertools import combinations

class Day9(Solver):
    def calculate_area(self, vertex1, vertex2) -> int:
        x0, y0 = vertex1
        x1, y1 = vertex2
        return (abs(x0 - x1) + 1) * (abs(y0 - y1) + 1)

    def solve(self) -> None:
        vertices = [tuple(int(x) for x in line.split(',')) for line in self.lines]

        self.part1 = max(
            self.calculate_area(p0, p1)
            for p0, p1 in combinations(vertices, 2)
        )

        edges = list(zip(vertices, vertices[1:] + [vertices[0]]))

        vertical_edges = [
            (x0, min(y0, y1), max(y0, y1))
            for (x0, y0), (x1, y1) in edges
            if x0 == x1
        ]

        horizontal_edges = [
            (y0, min(x0, x1), max(x0, x1))
            for (x0, y0), (x1, y1) in edges
            if y0 == y1
        ]

        for (x0, y0), (x1, y1) in combinations(vertices, 2):
            min_x = min(x0, x1) + 0.5
            max_x = max(x0, x1) - 0.5
            min_y = min(y0, y1) + 0.5
            max_y = max(y0, y1) - 0.5

            if min_x > max_x or min_y > max_y:
                continue

            crosses = False

            for vx, vy0, vy1 in vertical_edges:
                if min_x <= vx <= max_x:
                    if (vy0 <= min_y <= vy1) or (vy0 <= max_y <= vy1):
                        crosses = True
                        break

            if not crosses:
                for hy, hx0, hx1 in horizontal_edges:
                    if min_y <= hy <= max_y:
                        if (hx0 <= min_x <= hx1) or (hx0 <= max_x <= hx1):
                            crosses = True
                            break

            if not crosses:
                area = self.calculate_area((x0, y0), (x1, y1))
                self.part2 = max(self.part2, area)
    
Day9(2025, 9).run()
