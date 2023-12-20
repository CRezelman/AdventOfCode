class BroadCaster:
    def __init__(self, connections: list[str]) -> None:
        self.id = 'broadcaster'
        self.connections = connections
        self.enabled = True
        self.inputs: dict[str, bool] = {}

    def updateState(self, input: bool, _):
        return input

class FlipFlop:
    def __init__(self, id: str, connections: list[str]) -> None:
        self.id = id
        self.connections = connections
        self.enabled = False
        self.inputs: dict[str, bool] = {}

    def updateState(self, input: bool, _) -> bool:
        if input == True:
            return None
        elif input == False:
            self.enabled = not self.enabled
            if self.enabled:
                return True
            else: 
                return False


class Conjunction:
    def __init__(self, id: str, connections: list[str]) -> None:
        self.id = id
        self.connections = connections
        self.enabled = True
        self.inputs: dict[str, bool] = {}

    def updateState(self, input: bool, inputId: str) -> bool:
        self.inputs[inputId] = input

        if all(value == True for key, value in self.inputs.items()):
            return False
        else:
            return True
        

def day20():
    part1 = 0
    part2 = 0
    high = 0
    low = 0

    modules: dict[str, BroadCaster | FlipFlop | Conjunction] = {}

    with open('2023/inputs/day20.txt', 'r') as f:
        for line in f:
            module, connections = line.strip().split(' -> ')
            connections = connections.split(', ')

            if '%' in module:
                id = module.strip('%')
                current = FlipFlop(id, connections)
            elif '&' in module:
                id = module.strip('&')
                current = Conjunction(id, connections)
            else:
                id = 'broadcaster'
                current = BroadCaster(connections)
            
            modules[id] = current

        with open('2023/inputs/day20.txt', 'r') as f:
            for line in f:
                module, connections = line.strip().split(' -> ')
                id = module.strip('%&')

                for con in connections.split(', '):
                    if modules.get(con):
                        modules[con].inputs[id] = False



    for i in range(1000):
        low += 1
        q: list[tuple[BroadCaster | FlipFlop | Conjunction, bool]] = []
        currentModule = modules['broadcaster']
        signal = currentModule.updateState(0, None)
        q.append((currentModule, signal))
        # print(f'button -low-> broadcaster')
        
        while len(q):
            currentModule, signal = q.pop(0)
            for con in currentModule.connections:
                # print(f'{currentModule.id} -{"high" if signal else "low"}-> {con}')
                if signal:
                    high += 1
                else:
                    low += 1
                if modules.get(con):
                    newSignal = modules[con].updateState(signal, currentModule.id)
                    if newSignal is not None:
                        q.append((modules[con], newSignal))
        # print('\n')

    

    part1 = low*high
    return part1, part2

print(day20())