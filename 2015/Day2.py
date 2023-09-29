def day2():
    w = 0
    l = 0
    h = 0
    vol = 0
    sa = 0
    ribbon = 0
    mininmum = 0
    maximum = 0

    with open('2015/inputs/day2.txt') as f:
        for line in f:
            l, w, h = line.split('x')
            mininmum = min(int(l)*int(w), int(w)*int(h), int(h)*int(l))
            maximum = max(int(l), int(w), int(h))
            vol = int(l)*int(w)*int(h)
            sa += 2*int(l)*int(w) + 2*int(w)*int(h) + \
                2*int(h)*int(l) + mininmum
            ribbon += 2*int(l) + 2*int(w) + 2*int(h) - 2*maximum + vol
    return sa, ribbon


print(day2())
