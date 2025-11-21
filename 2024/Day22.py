"""Day 22 Solve"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines


def next_secret(s: int) -> int:
    MASK = (1 << 24) - 1
    s = ((s << 6) ^ s) & MASK
    s = ((s >> 5) ^ s) & MASK
    s = ((s << 11) ^ s) & MASK
    return s

def day22():
    """Day 22"""
    part1 = 0
    part2 = 0
    lines = read_lines(2024, 22)
    prices_list = []

    for line in lines:
        secret_number = int(line)
        prices = []

        for _ in range(2000):
            secret_number = next_secret(secret_number)
            prices.append(secret_number % 10)

        prices_list.append(prices)
        part1 += secret_number

    scores = {}

    for prices in prices_list:
        diffs = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        seen = set()

        for i in range(len(diffs) - 3):
            pattern = (
                diffs[i],
                diffs[i + 1],
                diffs[i + 2],
                diffs[i + 3]
            )
            if pattern in seen:
                continue

            seen.add(pattern)
            price_end = prices[i + 4]
            scores[pattern] = scores.get(pattern, 0) + price_end

    best_pattern, best_score = max(scores.items(), key=lambda x: x[1])
    print(f"Best pattern: {best_pattern} with score {best_score}")

    part2 = best_score

    return part1, part2

print(day22())
