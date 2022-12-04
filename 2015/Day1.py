def day1():
    floor = 0
    pos = 0
    with open('2015/day1.txt') as f:
        for index, char in enumerate(f.readline()):
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            
            if floor < 0 and pos == 0:
                pos = index + 1
        
    return floor, pos


print(day1())