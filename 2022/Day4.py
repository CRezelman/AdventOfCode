
class Sections():
    class Section:
        start = 0
        end = 0
    
    elf1 = Section()
    elf2 = Section()

    def __str__(self) -> str:
        return str(self.__dict__)

class Sum:
    part1 = 0
    part2 = 0

    def __str__(self) -> str:
        return str(self.__dict__)

def day4():
    sum = Sum()
    with open('2022/inputs/day4.txt') as f:
        for line in f:
            sections = Sections()
            elves = line.strip('\n').split(',')
            for i, elf in enumerate(elves):
                section = elf.split('-')
                if (i == 0):
                    sections.elf1.start = int(section[0])
                    sections.elf1.end = int(section[1])
                elif (i == 1):
                    sections.elf2.start = int(section[0])
                    sections.elf2.end = int(section[1])
        
            if ((sections.elf1.start >= sections.elf2.start) and (sections.elf1.end <= sections.elf2.end)) or ((sections.elf2.start >= sections.elf1.start) and (sections.elf2.end <= sections.elf1.end)):
                sum.part1 += 1

            if ((sections.elf2.start >= sections.elf1.start) and (sections.elf2.start <= sections.elf1.end)) or ((sections.elf1.start >= sections.elf2.start) and (sections.elf1.start <= sections.elf2.end)):
                sum.part2 += 1

    return sum

print(day4())