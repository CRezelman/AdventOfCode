
def charToPriority(char) -> int:
    if (ord(char) >= 65 and ord(char) <= 90):
        return (ord(char) - 38)
    elif (ord(char) >= 97 and ord(char) <= 122):
        return (ord(char) - 96)

class Sum:
    part1 = 0
    part2 = 0

    def __str__(self) -> str:
        return str(self.__dict__)

def day3():
    bag = []
    sum = Sum()
    with open('2022/day3.txt') as f:
        for index, line in enumerate(f):
            for char in line[:len(line)//2]:
                if char in line[len(line)//2:]:
                    sum.part1 += charToPriority(char)
                    break
            
            bag.append(line)
            if ((index + 1) % 3 == 0):
                for char in bag[0]:
                    if char in bag[1] and char in bag[2]:
                        sum.part2 += charToPriority(char)
                        break
                bag.clear()

    return sum

print(day3())
