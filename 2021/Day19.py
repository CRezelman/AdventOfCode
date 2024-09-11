"""Day 19"""

class Scanner:
    """Scanner"""
    def __init__(self, number: int) -> None:
        self.number = number
        self.beacons = []

    def add_beacon(self, x: int, y: int ,z: int):
        """Detected Beacon"""
        self.beacons.append((x, y, z))

def parse_input(lines) -> list[Scanner]:
    """Parse input file"""
    scanners: list[Scanner] = []

    for line in lines:
        if line.startswith("--- scanner"):
            scanner_number = int(line.split()[2])
            current_scanner = Scanner(scanner_number)
            scanners.append(current_scanner)
        elif line and current_scanner is not None:
            coordinates = tuple(map(int, line.split(',')))
            current_scanner.add_beacon(*coordinates)
    return scanners



def day19():
    """Day 19 Solve"""
    part1 = 0
    part2 = 0

    lines = open('2021/inputs/day19.txt', 'r').read().splitlines()
    scanners = parse_input(lines)

    for scanner1 in scanners:
        for scanner2 in scanners:
            if scanner1 != scanner2:
                print("Compare scanners to find")

    return (part1, part2)

print(day19())
