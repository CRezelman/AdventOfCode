import math

class Monkey0:
    id = 0
    inspected = 0

    def __init__(self, items: list):
        self.items = items

    def add(self, item):
        self.items.append(item)
    
    def operation(self, item):
        return item * 17

    def test(self, item):
        if item % 3 == 0:
            monkey4.add(item)
        else:
            monkey2.add(item)

class Monkey1:
    id = 1
    inspected = 0
    
    def __init__(self, items: list):
        self.items = items
    
    def add(self, item):
        self.items.append(item)
    
    def operation(self, item):
        return item * 11

    def test(self, item):
        if item % 5 == 0:
            monkey3.add(item)
        else:
            monkey5.add(item)

class Monkey2:
    id = 2
    inspected = 0
    
    def __init__(self, items: list):
        self.items = items

    def add(self, item):
        self.items.append(item)   

    def operation(self, item):
        return item + 4

    def test(self, item):
        if item % 2 == 0:
            monkey6.add(item)
        else:
            monkey4.add(item)
        

class Monkey3:
    id = 3
    inspected = 0
    
    def __init__(self, items: list):
        self.items = items

    def add(self, item):
        self.items.append(item)
    
    def operation(self, item):
        return item * item

    def test(self, item):
        if item % 13 == 0:
            monkey0.add(item)
        else:
            monkey5.add(item)
        

class Monkey4:
    id = 4
    inspected = 0
    
    def __init__(self, items: list):
        self.items = items

    def add(self, item):
        self.items.append(item)
    
    def operation(self, item):
        return item + 7

    def test(self, item):
        if item % 11 == 0:
            monkey7.add(item)
        else:
            monkey6.add(item)
        

class Monkey5:
    id = 5
    inspected = 0
    
    def __init__(self, items: list):
        self.items = items

    def add(self, item):
        self.items.append(item)
    
    def operation(self, item):
        return item + 8

    def test(self, item):
        if item % 17 == 0:
            monkey0.add(item)
        else:
            monkey2.add(item)

class Monkey6:
    id = 6
    inspected = 0
    
    def __init__(self, items: list):
        self.items = items

    def add(self, item):
        self.items.append(item)
    
    def operation(self, item):
        return item + 5

    def test(self, item):
        if item % 19 == 0:
            monkey7.add(item)
        else:
            monkey1.add(item)

class Monkey7:
    id = 7
    inspected = 0
    
    def __init__(self, items: list):
        self.items = items

    def add(self, item):
        self.items.append(item)
    
    def operation(self, item):
        return item + 3

    def test(self, item):
        if item % 7 == 0:
            monkey1.add(item)
        else:
            monkey3.add(item)


monkey0 = Monkey0([99, 67, 92, 61, 83, 64, 98])
monkey1 = Monkey1([78, 74, 88, 89, 50])
monkey2 = Monkey2([98, 91])
monkey3 = Monkey3([59, 72, 94, 91, 79, 88, 94, 51])
monkey4 = Monkey4([95, 72, 78])
monkey5 = Monkey5([76])
monkey6 = Monkey6([69, 60, 53, 89, 71, 88])
monkey7 = Monkey7([72, 54, 63, 80])    

def part(rounds, worry):
    for round in range(rounds):
        for item in monkey0.items:
            newItem = monkey0.operation(item)
            if worry:
                newItem = math.floor(newItem/3)
            monkey0.test(newItem)
            monkey0.inspected += 1
        monkey0.items.clear()

        for item in monkey1.items:
            newItem = monkey1.operation(item)
            if worry:
                newItem = math.floor(newItem/3)
            monkey1.test(newItem)
            monkey1.inspected += 1
        monkey1.items.clear()

        for item in monkey2.items:
            newItem = monkey2.operation(item)
            if worry:
                newItem = math.floor(newItem/3)
            monkey2.test(newItem)
            monkey2.inspected += 1
        monkey2.items.clear()

        for item in monkey3.items:
            newItem = monkey3.operation(item)
            if worry:
                newItem = math.floor(newItem/3)
            monkey3.test(newItem)
            monkey3.inspected += 1
        monkey3.items.clear()

        for item in monkey4.items:
            newItem = monkey4.operation(item)
            if worry:
                newItem = math.floor(newItem/3)
            monkey4.test(newItem)
            monkey4.inspected += 1
        monkey4.items.clear()

        for item in monkey5.items:
            newItem = monkey5.operation(item)
            if worry:
                newItem = math.floor(newItem/3)
            monkey5.test(newItem)
            monkey5.inspected += 1
        monkey5.items.clear()

        for item in monkey6.items:
            newItem = monkey6.operation(item)
            if worry:
                newItem = math.floor(newItem/3)
            monkey6.test(newItem)
            monkey6.inspected += 1
        monkey6.items.clear()

        for item in monkey7.items:
            newItem = monkey7.operation(item)
            if worry:
                newItem = math.floor(newItem/3)
            monkey7.test(newItem)
            monkey7.inspected += 1
        monkey7.items.clear()


def day11():
    part1 = 0
    inspected = []

    monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
    part(10000, False)

            
    for monkey in monkeys:
        inspected.append(monkey.inspected)

    inspected.sort(reverse=1)
    part1 = inspected[0]*inspected[1]

    return part1

print(day11())
