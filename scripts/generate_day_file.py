"""Generates File for a new Day"""
import sys
import os

def generate_day_file(year: int, day: int):
    """Generates File for a new Day"""
    content = f'''"""Day {day} Solve"""
from utilities.input import read_lines

def day{day}():
    """Day {day}"""
    part1 = 0
    part2 = 0
    lines = read_lines({year}, {day})

    return part1, part2

print(day{day}())

'''

    directory = os.path.join(os.path.dirname(__file__), f"../{year}")
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    filename = os.path.join(directory, f"Day{day}.py")
    with open(filename, 'w', encoding= 'utf-8') as file:
        file.write(content)
    print(f"File {filename} has been created.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scripts/generate_day_file.py <year> <day>")
    else:
        year = sys.argv[1]
        day = sys.argv[2]
        generate_day_file(year, day)
