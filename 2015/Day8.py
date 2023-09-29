def day8():
    code_total = 0
    mem_total = 0
    encode_total = 0
    with open('2015/inputs/day8.txt') as f:
        for line in f:
            line = line.strip('\n')
            code_total += len(line)
            encode_line = '"' + \
                line.replace('\\', '\\\\').replace(
                    '\"', '\\\"').replace('"', '\"') + '"'
            encode_total += len(encode_line)
            mem_total += len(eval(line))

    return (code_total - mem_total), (encode_total - code_total)


print(day8())
