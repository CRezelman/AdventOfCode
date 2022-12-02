def day2():
    score = [0, 0]
    with open('2022/day2.txt') as f:
        for line in f:
            round = line.strip('\n').split(' ')
            if (round[1] == 'X'):
                score[0] += 1
                score[1] += 0
                if (round[0] == 'A'):
                    score[0] += 3
                    score[1] += 3
                elif (round[0] == 'B'):
                    score[0] += 0
                    score[1] += 1
                elif (round[0] == 'C'):
                    score[0] += 6
                    score[1] += 2
            elif (round[1] == 'Y'):
                score[0] += 2
                score[1] += 3
                if (round[0] == 'A'):
                    score[0] += 6
                    score[1] += 1
                elif (round[0] == 'B'):
                    score[0] += 3
                    score[1] += 2
                elif (round[0] == 'C'):
                    score[0] += 0
                    score[1] += 3
            elif (round[1] == 'Z'):
                score[0] += 3
                score[1] += 6
                if (round[0] == 'A'):
                    score[0] += 0
                    score[1] += 2
                elif (round[0] == 'B'):
                    score[0] += 6
                    score[1] += 3
                elif (round[0] == 'C'):
                    score[0] += 3
                    score[1] += 1

    return score

print(day2())