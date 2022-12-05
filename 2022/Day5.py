def day5():
    topCrates1 = ''
    topCrates2 = ''

    stacks1 = [[], [], [], [], [], [], [], [], []]
    stacks2 = [[], [], [], [], [], [], [], [], []]

    with open('2022/day5.txt') as f:
        for i, line in enumerate(f):
            if i < 8:
                count = 0
                for index, char in enumerate(line):
                    if index % 4 == 1:
                        if char != ' ':
                            stacks1[count].insert(0, char)
                            stacks2[count].insert(0, char)
                        count += 1

            if i >= 10:
                line = line.split(' ')
                move = line[1]
                source = line[3]
                target = line[5]
                tempStack = ['']*int(move)
                for j in range(int(move)):
                    stacks1[int(target)-1].append(stacks1[int(source)-1].pop())
                    tempStack[int(move) - (j + 1)] = stacks2[int(source)-1].pop()
                
                for temp in tempStack:
                    stacks2[int(target)-1].append(temp)
        
        for stack in stacks1:
            topCrates1 += stack[len(stack)-1]
        for stack in stacks2:
            topCrates2 += stack[len(stack)-1]

    return topCrates1, topCrates2

print(day5())
