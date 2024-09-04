"""Day 14"""
from collections import Counter, defaultdict

def day14():
    """Day 14"""
    ITERATIONS_P1 = 10
    ITERATIONS_P2 = 40
    reactions = {}

    lines = open('2021/inputs/day14demo.txt', 'r').read().splitlines()
    prev_polymer = lines[0]
    for line in lines[2:]:
        reaction, insert = line.split(' -> ')
        reactions[reaction] = insert

    # Initialize pair counts
    pair_counts = Counter([prev_polymer[i:i+2] for i in range(len(prev_polymer) - 1)])
    element_counts = Counter(prev_polymer)

    def run_iterations(iterations):
        nonlocal pair_counts, element_counts
        for _ in range(iterations):
            new_pair_counts = defaultdict(int)
            for pair, count in pair_counts.items():
                if pair in reactions:
                    insert = reactions[pair]
                    new_pair1 = pair[0] + insert
                    new_pair2 = insert + pair[1]
                    new_pair_counts[new_pair1] += count
                    new_pair_counts[new_pair2] += count
                    element_counts[insert] += count
                else:
                    new_pair_counts[pair] += count
            pair_counts = new_pair_counts

    # Run the iterations
    run_iterations(ITERATIONS_P1)  # For part 1
    part1 = max(element_counts.values()) - min(element_counts.values())

    run_iterations(ITERATIONS_P2 - ITERATIONS_P1)  # For part 2
    part2 = max(element_counts.values()) - min(element_counts.values())

    return part1, part2

print(day14())
