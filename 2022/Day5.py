def day5():
    topCrates1 = ''
    topCrates2 = ''
    stacks1 = [
        ['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'],
        ['N', 'V', 'G', 'P', 'H', 'W', 'B'],
        ['F', 'W', 'B', 'J', 'G'],
        ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'],
        ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'],
        ['B', 'C', 'W', 'G', 'F', 'S'],
        ['H', 'T', 'P', 'M', 'Q', 'B', 'W'],
        ['F', 'S', 'W', 'T'],
        ['N', 'C', 'R']
    ]
    stacks2 = [
        ['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'],
        ['N', 'V', 'G', 'P', 'H', 'W', 'B'],
        ['F', 'W', 'B', 'J', 'G'],
        ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'],
        ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'],
        ['B', 'C', 'W', 'G', 'F', 'S'],
        ['H', 'T', 'P', 'M', 'Q', 'B', 'W'],
        ['F', 'S', 'W', 'T'],
        ['N', 'C', 'R']
    ]

    with open('2022/day5.txt') as f:
        for i, line in enumerate(f):
            if i >= 10:
                line = line.strip('\n').split(' ')
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
