def day8():
    part1 = 0
    part2 = 0
    
    with open('2021/inputs/day8.txt') as f:
        for line in f:
            line = line.strip('\n')
            input_str, output_str = line.split(' | ')
            
            input_digits = input_str.split()
            output_digits = output_str.split()

            part1 += sum(1 for digit in output_digits if len(digit) in [2, 4, 3, 7])

            one = next(digit for digit in input_digits if len(digit) == 2)
            four = next(digit for digit in input_digits if len(digit) == 4)
            seven = next(digit for digit in input_digits if len(digit) == 3)
            eight = next(digit for digit in input_digits if len(digit) == 7)
            twoThreeFive = [digit for digit in input_digits if len(digit) == 5]
            zeroSixNine = [digit for digit in input_digits if len(digit) == 6]

            three = next((digit for digit in twoThreeFive if all(char in digit for char in one)), None)
            twoThreeFive.remove(three) if three is not None else None

            five = next((digit for digit in twoThreeFive if all(char in digit for char in set(four) - set(one))), None)
            twoThreeFive.remove(five) if five is not None else None
            two = twoThreeFive.pop() if five is not None else None

            six = next((digit for digit in zeroSixNine if not all(char in digit for char in one)), None)
            zeroSixNine.remove(six) if six is not None else None

            nine = next((digit for digit in zeroSixNine if all(char in digit for char in four)), None)
            zeroSixNine.remove(nine) if nine is not None else None
            zero = zeroSixNine.pop() if nine is not None else None

            numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
            
            result = ''.join(str(i) for digit in output_digits for i, num in enumerate(numbers) if sorted(num) == sorted(digit))
            part2 += int(result) if result else 0

    return part1, part2

print(day8())
