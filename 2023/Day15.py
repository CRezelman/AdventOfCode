def hash(item: str):
    value = 0
    for char in item:
        value += ord(char)
        value *= 17
        value %= 256
    return value


def day15(): 
    part1 = 0
    part2 = 0

    hashMap: dict[int, list[dict[str, int]]] = {}

    data = open('2023/inputs/day15.txt').read().strip().split(',')

    part1 = sum(hash(item) for item in data)

    for item in data:
        if '-' in item:
            label, _ = item.split('-')
            if hashMap.get(hash(label)):
                values = hashMap[hash(label)]

                for i, value in enumerate(values):
                    if value.get(label):
                        values.pop(i)
 
        elif '=' in item:
            label, lens = item.split('=')
            if not hashMap.get(hash(label)):
                hashMap[hash(label)] = [{label: int(lens)}]
            else:
                values = hashMap[hash(label)]
                for i, value in enumerate(values):
                    if value.get(label):
                        value[label] = int(lens)
                        break
                else:
                    hashMap[hash(label)] += [{label: int(lens)}]

    for item in hashMap.items():
        boxNo = item[0] + 1
        for i, slot in enumerate(item[1]):
            slotNo = i + 1
            focalLength = next(iter(slot.values()))
            part2 += boxNo*slotNo*focalLength


    return part1, part2

print(day15())

