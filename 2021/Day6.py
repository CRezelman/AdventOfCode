def day6(days: int): 
    with open('2021/inputs/day6.txt', 'r') as f:
        data = f.readlines()
        data = list(map(int, data[0].strip().split(",")))

    fish = [data.count(i) for i in range(9)]
    for i in range(days):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)
        assert len(fish) == 9
    return sum(fish)


print(day6(80), day6(256))