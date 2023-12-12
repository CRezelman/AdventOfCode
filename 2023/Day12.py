from functools import lru_cache
    
@lru_cache(maxsize=None)
def count(springs, group):
    if springs == '':
        return 1 if group == () else 0
    
    if group == ():
        return 0 if '#' in springs else 1
    
    result = 0

    if springs[0] in '.?':
        result += count(springs[1:], group)

    if springs[0] in '#?':
        if group[0] <= len(springs) and '.' not in springs[:group[0]] and (group[0] == len(springs) or springs[group[0]] != '#'):
            result += count(springs[group[0] + 1:], group[1:])

    return result


def day12(): 
    part1 = 0
    part2 = 0
    with open('2023/inputs/day12.txt', 'r') as f:
       for line in f:
           springs, group = line.strip().split()
           group = tuple(map(int, group.split(',')))
           part1 += count(springs, group)
           part2 += count('?'.join([springs] * 5), group * 5)

    return part1, part2

print(day12())
