
def day1():
    result = 0
    num1 = 0
    num2 = 0
    numChars = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open('2023/inputs/day1.txt') as f:
        for line in f:
            line = line.strip('\n')
            left = ''
            for char in line:
                if num1: break
                left += char
                for i, numChar in enumerate(numChars):
                    if numChar in left:
                        num1 = str(i+1)
                        break
                if char.isdigit():
                    num1 = char
                    break
 
            line = line[::-1]
            right = ''
            for char in line:
                if num2: break
                right += char
                for i, numChar in enumerate(numChars):
                    revChar = right[::-1]
                    if numChar in revChar:
                        num2 = str(i+1)
                        break
                if char.isdigit():
                    num2 = char
                    break
    
                    
                
            num = int(str(num1) + str(num2))
            num1 = 0 
            num2 = 0 
            result += num

    return result

print(day1())