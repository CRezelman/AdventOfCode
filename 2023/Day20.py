from abc import ABC, abstractclassmethod
from copy import deepcopy
import math

class Module(ABC):
    def __init__(self, id: str, connections: list[str], enabled: bool) -> None:
        self.id = id
        self.connections = connections
        self.enabled = enabled
        self.inputs: dict[str, bool] = {}

    @abstractclassmethod
    def updateState(self, input: bool, inputId: str): 
        pass

class BroadCaster(Module):
    def __init__(self, connections: list[str]) -> None:
        super().__init__('broadcaster', connections, True)
    
    def updateState(self, input: bool, inputId: str):
        return input
    

class FlipFlop(Module):
    def __init__(self, id: str, connections: list[str]) -> None:
        super().__init__(id, connections, False)

    def updateState(self, input: bool, inputId: str) -> bool:
        if input == True:
            return None
        self.enabled = not self.enabled
        return self.enabled
            

class Conjunction(Module):
    def __init__(self, id: str, connections: list[str]) -> None:
        super().__init__(id, connections, True)

    def updateState(self, input: bool, inputId: str) -> bool:
        self.inputs[inputId] = input
        return not all(value == True for key, value in self.inputs.items())

        
def solve(iterations: int, modules: dict[str, Module]):
    high = 0
    low = 0
    moduleRx = {}
    for i in range(iterations):
        low += 1
        currentModule = modules['broadcaster']
        signal = currentModule.updateState(0, None)
        q: list[tuple[Module, bool]] = [(currentModule, signal)]
        
        while len(q):
            currentModule, signal = q.pop(0)
            for con in currentModule.connections:
                if signal:
                    high += 1
                else:
                    low += 1
                if modules.get(con):
                    if signal == True and modules[con].id == 'zp':
                        if not moduleRx.get(currentModule.id):
                            moduleRx[currentModule.id] = i + 1
                        if len(moduleRx) == len(modules[con].inputs):
                            return math.lcm(*moduleRx.values())
                    newSignal = modules[con].updateState(signal, currentModule.id)
                    if newSignal is not None:
                        q.append((modules[con], newSignal))
    
    return high*low
        

def day20():
    inputFile = '2023/inputs/day20.txt'

    modules: dict[str, BroadCaster | FlipFlop | Conjunction] = {}
    modulesCopy: dict[str, BroadCaster | FlipFlop | Conjunction] = {}

    with open(inputFile, 'r') as f:
        for line in f:
            module, connections = line.strip().split(' -> ')
            connections = connections.split(', ')
            id = module.strip('&%')

            if '%' in module:
                current = FlipFlop(id, connections)
            elif '&' in module:
                current = Conjunction(id, connections)
            else:
                id = 'broadcaster'
                current = BroadCaster(connections)
            
            modules[id] = current

        with open(inputFile, 'r') as f:
            for line in f:
                module, connections = line.strip().split(' -> ')
                id = module.strip('%&')

                for con in connections.split(', '):
                    if modules.get(con):
                        modules[con].inputs[id] = False

        modulesCopy = deepcopy(modules)

    part1 = solve(1000, modules)
    part2 = solve(5000, modulesCopy)

    return part1, part2

print(day20())