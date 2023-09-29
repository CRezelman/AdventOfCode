def day5():
    nice = 0
    nice2 = 0
    notAllowed = ['ab', 'cd', 'pq', 'xy']
    vowels = ['a', 'e', 'i', 'o', 'u']
    with open('2015/inputs/day5.txt') as f:
        for ind, line in enumerate(f):
            line = line.strip('\n')
            vowelsFound = 0
            doubleFound = 0
            badFound = 0
            pairsFound = 0
            repeatsSplitFound = 0
            pairSet = set()
            prevChar = ''
            for bad in notAllowed:
                if bad in line:
                    badFound = 1

            for char in line:
                if char in vowels:
                    vowelsFound += 1
                if prevChar == char:
                    doubleFound = 1
                prevChar = char

            if badFound == 0 and vowelsFound >= 3 and doubleFound:
                nice += 1
            triples = 0
            for i, char in enumerate(line):
                if i >= 1:
                    substring = line[i-1:i+1]
                    pairSet.add(substring)
                if i >= 2:
                    sub = line[i-2:i+1]
                    if sub[0] == sub[1] and sub[1] == sub[2]:
                        triples += 1

            if len(pairSet) < ((len(line)-1) - triples):
                pairsFound += 1

            for i, char in enumerate(line):
                if i >= 2:
                    substring = line[i-2:i+1]
                    if substring[0] == substring[2]:
                        repeatsSplitFound = 1

            if pairsFound and repeatsSplitFound:
                nice2 += 1

    return nice, nice2


print(day5())
