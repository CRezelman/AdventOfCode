import itertools


def day10():
    s = "1321131112"
    for i in range(50):
        s = ''.join([str(len(list(g)))+k for k, g in itertools.groupby(s)])

    return len(s)


print(day10())
