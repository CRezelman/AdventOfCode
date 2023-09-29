AND = ' AND '
OR = ' OR '
LSHIFT = ' LSHIFT '
RSHIFT = ' RSHIFT '
NOT = 'NOT'

wires = {}
with open('2015/inputs/day7.txt') as f:
    for line in f:
        line = line.strip('\n')
        signal, wire = line.split(' -> ')
        wires[wire] = signal

# wires['b'] = 46065


def solve(wire):
    if wire.isnumeric():
        return int(wire)

    signal = wires[wire]

    if type(signal) == int or signal.isnumeric():
        wires[wire] = int(signal)

    else:
        if AND in signal:
            a, b = signal.split(AND)
            wires[wire] = solve(a) & solve(b)

        elif OR in signal:
            a, b = signal.split(OR)
            wires[wire] = solve(a) | solve(b)

        elif LSHIFT in signal:
            a, b = signal.split(LSHIFT)
            wires[wire] = solve(a) << int(b)

        elif RSHIFT in signal:
            a, b = signal.split(RSHIFT)
            wires[wire] = solve(a) >> int(b)

        elif NOT in signal:
            _, a = signal.split()
            wires[wire] = ~(solve(a))

        else:
            wires[wire] = solve(signal)

    return wires[wire]


print(solve('a'))
