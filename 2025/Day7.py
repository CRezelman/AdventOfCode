"""Day 7 Solve"""
from utilities.solver import Solver
from collections import deque

class Day7(Solver):
    def solve(self) -> None:
        start = self.grid.find_in_grid("S")
        queue = deque([start])
        visited = set()

        while queue:
            y, x = queue.popleft()
            ny, nx = y + 1, x

            if not self.grid.is_in_bounds(ny, nx):
                continue

            if self.grid.get_value(ny, nx) == '^':
                if (ny, nx) not in visited:
                    self.part1 += 1
                    visited.add((ny, nx))

                queue.append((ny, nx - 1))
                queue.append((ny, nx + 1))

            else:
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((ny, nx))


        current = [0] * self.grid.cols
        current[start[1]] = 1

        for r in range(self.grid.rows - 1):
            next_row = [0] * self.grid.cols

            for c in range(self.grid.cols):
                count = current[c]
                if count == 0:
                    continue

                if self.grid.get_value(r, c) == '^':
                    if c > 0:
                        next_row[c - 1] += count
                    if c < self.grid.cols - 1:
                        next_row[c + 1] += count
                else:
                    next_row[c] += count

            current = next_row

        self.part2 = sum(current)

    
Day7(2025, 7).run()
