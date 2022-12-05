def day5():
    nice = 0
    nice2 = 0
    notAllowed = ['ab', 'cd', 'pq', 'xy']
    vowels = ['a', 'e', 'i', 'o', 'u']
    with open('2015/day5.txt') as f:
        for line in f:
            vowelsFound = 0
            doubleFound = 0
            badFound = 0
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
                nice +=1

            # for i, char in enumerate(line):
            #     if(i <= 13):
            #         if line[i] == line[i+1]:
            #             substr = line[i] + line[i+1]
            #             if substr in line[2:len(line)]:
            #                 nice2 += 1
            #         elif line[i] == line[i+2]:
            #             nice2 +=1

    return nice, nice2


print(day5())