"""Day 21 Solve"""

import os
import sys
from collections import deque, defaultdict
from functools import lru_cache

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines


NUMERIC_KEYS = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2),
}

ROBOT_KEYS = {
                 '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}

MOVES = [
    ("^", -1, 0),
    ("v", 1, 0),
    ("<", 0, -1),
    (">", 0, 1),
]


def build_all_shortest_paths(key_positions):
    all_map = {}
    delta_to_char = {(-1, 0): "^", (1, 0): "v", (0, -1): "<", (0, 1): ">"}

    for src_key, src_pos in key_positions.items():
        q = deque([src_pos])
        dist = {src_pos: 0}
        parents = defaultdict(list)

        while q:
            y, x = q.popleft()
            d = dist[(y, x)]
            for ch, dy, dx in MOVES:
                ny, nx = y + dy, x + dx
                if (ny, nx) not in key_positions.values():
                    continue
                if (ny, nx) not in dist:
                    dist[(ny, nx)] = d + 1
                    parents[(ny, nx)].append((y, x))
                    q.append((ny, nx))
                else:
                    if dist[(ny, nx)] == d + 1:
                        parents[(ny, nx)].append((y, x))

        for dst_key, dst_pos in key_positions.items():
            if dst_pos not in dist:
                all_map[(src_key, dst_key)] = []
                continue

            paths = []

            def backtrack_coords(cur_pos, acc):
                if cur_pos == src_pos:
                    coords = list(reversed(acc))
                    paths.append(coords)
                    return
                for p in parents[cur_pos]:
                    backtrack_coords(p, acc + [p])

            backtrack_coords(dst_pos, [dst_pos])

            move_strings = []
            for coords in paths:
                moves = []
                for i in range(len(coords) - 1):
                    y0, x0 = coords[i]
                    y1, x1 = coords[i + 1]
                    dy, dx = (y1 - y0), (x1 - x0)
                    moves.append(delta_to_char[(dy, dx)])
                moves.append("A")
                move_strings.append("".join(moves))

            all_map[(src_key, dst_key)] = sorted(set(move_strings))

    return all_map


NUMERIC_PATHS = build_all_shortest_paths(NUMERIC_KEYS)
ROBOT_PATHS = build_all_shortest_paths(ROBOT_KEYS)



@lru_cache(maxsize=None)
def min_expanded_length_move_string(move_string: str, depth: int) -> int:
    if depth == 0:
        return len(move_string)

    total = 0
    prev = 'A'
    for ch in move_string:
        candidates = ROBOT_PATHS.get((prev, ch), [])
        if not candidates:
            return float('inf')
        best_candidate_len = float('inf')
        for cand in candidates:
            cand_len = min_expanded_length_move_string(cand, depth - 1)
            if cand_len < best_candidate_len:
                best_candidate_len = cand_len
        total += best_candidate_len
        prev = ch
    return total


@lru_cache(maxsize=None)
def min_expanded_length_between_keys(src_key: str, dst_key: str, top_level: bool, depth: int) -> int:
    mapping = NUMERIC_PATHS if top_level else ROBOT_PATHS
    candidates = mapping.get((src_key, dst_key), [])
    if not candidates:
        return float('inf')
    best = float('inf')
    for cand in candidates:
        cand_len = min_expanded_length_move_string(cand, depth)
        if cand_len < best:
            best = cand_len
    return best


def length_of_final_input_for_code(code: str, expansion_depth: int) -> int:
    total = 0
    prev = 'A'
    for ch in code:
        step_len = min_expanded_length_between_keys(prev, ch, top_level=True, depth=expansion_depth)
        total += step_len
        prev = ch
    return total


def day21():
    lines = read_lines(2024, 21)
    part1 = 0
    part2 = 0

    for line in lines:
        code = line.strip()
        numeric_value = int(code.rstrip('A'))
        l1 = length_of_final_input_for_code(code, expansion_depth=2)
        l2 = length_of_final_input_for_code(code, expansion_depth=25)

        part1 += numeric_value * l1
        part2 += numeric_value * l2

    return part1, part2

print(day21())
