class Part:
    def __init__(self, x: int, m: int, a: int, s: int) -> None:
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def sum(self) -> int:
        return int(self.x) + int(self.m) + int(self.a) + int(self.s)


def solve(workflow: list[tuple[str, str]], part: Part):
    for condition, result in workflow:
        if condition == None: return result
        test = condition.replace('x', part.x).replace('m', part.m).replace('a', part.a).replace('s', part.s)
        if eval(test):
            return result

def day18():
    part1 = 0
    part2 = 0
    workflows: dict[str, list[tuple[str, str]]] = {}
    parts: list[Part] = []

    with open('2023/inputs/day19.txt', 'r') as file:
        newLine = 0
        for line in file:
            if newLine == 0 and line != '\n':
                key, logic = line.strip('}\n').split('{')
                result = []
                for item in logic.split(','):
                    if ':' in item:
                        item = item.split(':')
                        result.append((item[0], item[1]))
                    else: 
                        result.append((None, item))
                workflows[key] = result
            elif line == '\n': newLine +=1
            else:
                line = line.strip('}\n').strip('{').split(',')
                x = line[0].split('=')[1]
                m = line[1].split('=')[1]
                a = line[2].split('=')[1]
                s = line[3].split('=')[1]
                parts.append(Part(x, m, a, s))

    for part in parts:
        current = workflows['in']
        while True:
            result = solve(current, part)
            if result == 'A':
                part1 += part.sum()
                break
            if result == 'R':
                break
            else:
                current = workflows[result]

    return part1, part2

print(day18())