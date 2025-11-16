"""Day 15 Solve"""
import os
import sys
from dataclasses import dataclass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines

@dataclass
class Coordinate:
    x: int
    y: int

@dataclass
class CoordinateP2:
    x1: int
    x2: int
    y: int

    def __hash__(self):
        return hash((self.x1, self.x2, self.y))

@dataclass
class Warehouse:
    walls_p1: list[Coordinate]
    boxes_p1: list[Coordinate]
    robot_p1: Coordinate

    walls_p2: list[Coordinate]
    boxes_p2: list[CoordinateP2]
    robot_p2: Coordinate

    moves: str

    dirs = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }

    def simulate_p2(self, debug=False) -> None:
        """
        Simulate the warehouse operations for part 2 based on moves.
        Move robot to next position. If next position has a box, move the box in the same direction if possible.
        Move robots and boxes in the direction unless blocked by a wall. If blocked, skip the move.
        """

        for move in self.moves:
            if debug:
                self.render_warehouse_p2()
                print("Move:", move)
            dx, dy = self.dirs[move]
            next_pos = Coordinate(self.robot_p2.x + dx, self.robot_p2.y + dy)

            boxes_to_move: set[CoordinateP2] = set()
            check_pos = [next_pos]

            while True:
                if len(check_pos) == 0:
                    break

                cp = check_pos.pop(0)

                if cp in self.walls_p2:
                    boxes_to_move.clear()
                    break

                box = next((b for b in self.boxes_p2 if (b.x1 == cp.x or b.x2 == cp.x) and b.y == cp.y), None)
                if box:
                    boxes_to_move.add(box)
                    if dx == 0:  # Moving vertically
                        check_pos.append(Coordinate(box.x1, box.y + dy))
                        check_pos.append(Coordinate(box.x2, box.y + dy))
                    else:  # Moving horizontally
                        check_pos.append(Coordinate(cp.x + 2*dx, cp.y + dy))

                    continue

                if len(check_pos) > 0:
                    continue
                # Found empty space -> perform move
                self.robot_p2.x += dx
                self.robot_p2.y += dy
                for b in reversed(list(boxes_to_move)):
                    b.x1 += dx
                    b.x2 += dx
                    b.y += dy
                break
        if debug:
            self.render_warehouse_p2()

    def simulate_p1(self) -> None:
        """
        Simulate the warehouse operations based on moves.
        Move robot to next position. If next position has a box, move the box in the same direction if possible.
        Move robots and boxes in the direction unless blocked by a wall. If blocked, skip the move.
        """

        for move in self.moves:
            dx, dy = self.dirs[move]
            next_pos = Coordinate(self.robot_p1.x + dx, self.robot_p1.y + dy)

            boxes_to_move: list[Coordinate] = []
            check_pos = next_pos

            while True:
                if check_pos in self.walls_p1:
                    boxes_to_move.clear()
                    break

                # Found a box
                box = next((b for b in self.boxes_p1 if b.x == check_pos.x and b.y == check_pos.y), None)
                if box:
                    boxes_to_move.append(box)
                    check_pos = Coordinate(check_pos.x + dx, check_pos.y + dy)
                    continue

                # Found empty space -> perform move
                self.robot_p1.x += dx
                self.robot_p1.y += dy
                for b in reversed(boxes_to_move):
                    b.x += dx
                    b.y += dy
                break


    
    def render_warehouse_p2(self) -> None:
        """ print out the warehouse state for debugging, a wall is '#', box is '[' for x1 and ']' for x2, robot is '@', empty is '.'"""
        max_x = max([w.x for w in self.walls_p2] + [b.x2 for b in self.boxes_p2] + [self.robot_p2.x])
        max_y = max([w.y for w in self.walls_p2] + [b.y for b in self.boxes_p2] + [self.robot_p2.y])

        grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        for w in self.walls_p2:
            grid[w.y][w.x] = '#'
        for b in self.boxes_p2:
            grid[b.y][b.x1] = '['
            grid[b.y][b.x2] = ']'
        grid[self.robot_p2.y][self.robot_p2.x] = '@'

        for row in grid:
            print(''.join(row))
        print()


def parse_input(lines: list[str]) -> tuple[Warehouse, str]:
    blank_index = next(i for i, line in enumerate(lines) if not line.strip())
    grid_lines = lines[:blank_index]
    move_lines = lines[blank_index + 1:]

    walls_p1, boxes_p1, walls_p2, boxes_p2 = [], [], [], []
    robot_p1, robot_p2 = None, None

    for y, row in enumerate(grid_lines):
        for x, char in enumerate(row):
            match char:
                case '#':
                    walls_p1.append(Coordinate(x, y))
                    walls_p2.append(Coordinate(2*x, y))
                    walls_p2.append(Coordinate(2*x+1, y))
                case 'O':
                    boxes_p1.append(Coordinate(x, y))
                    boxes_p2.append(CoordinateP2(2*x, 2*x+1, y))
                case '@':
                    robot_p1 = Coordinate(x, y)
                    robot_p2 = Coordinate(2*x, y)

    moves = ''.join(line.strip() for line in move_lines)
    return Warehouse(walls_p1, boxes_p1, robot_p1, walls_p2, boxes_p2, robot_p2, moves)


def day15():
    """Day 15"""
    part1 = 0
    part2 = 0
    lines = read_lines(2024, 15)

    warehouse: Warehouse = parse_input(lines)
    warehouse.simulate_p1()
    warehouse.simulate_p2()

    for box in warehouse.boxes_p1:
        part1 += box.x + 100*box.y
    for box in warehouse.boxes_p2:
        part2 += min(box.x1, box.x2) + 100*(box.y)

    return part1, part2

print(day15())
