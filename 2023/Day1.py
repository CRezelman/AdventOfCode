def processLine(line: str, part: int, reverse = False) -> str:
    numChars = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = 0
    substr = ''
    line = line[::-1] if reverse else line
    
    for char in line:
        if num and part == 2: break
        substr += char
        for i, numChar in enumerate(numChars):
            if numChar in (substr[::-1] if reverse else substr):
                num = str(i + 1)
                break

        if char.isdigit():
            num = char
            break
    return num

def day1(part: int) -> int:
    result = 0
    with open('2023/inputs/day1.txt') as f:
        for line in f:
            line = line.strip('\n')
            num1 = processLine(line, part, False)
            num2 = processLine(line, part, True)
            result += int(str(num1) + str(num2))

    return result

print(day1(1), day1(2))
