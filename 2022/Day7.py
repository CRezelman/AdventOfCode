"""Day 7 Solve"""
from utilities.solver import InputType, Solver
import networkx as nx

class Day7(Solver):

    def build_fs(self):
        G = nx.DiGraph()
        cwd = []

        def current_path():
            return "/"  + "/".join(cwd)

        G.add_node("/", type="dir", size=0)

        i = 0
        while i < len(self.lines):
            line = self.lines[i]

            if line.startswith("$ cd"):
                target = line.split()[-1]
                if target == "/":
                    cwd = []
                elif target == "..":
                    if cwd:
                        cwd.pop()
                else:
                    cwd.append(target)
                i += 1
                continue

            if line.startswith("$ ls"):
                i += 1
                while i < len(self.lines) and not self.lines[i].startswith("$"):
                    entry = self.lines[i].strip()
                    parent = current_path()

                    if entry.startswith("dir"):
                        _, name = entry.split()
                        path = parent.rstrip("/") + "/" + name
                        if path not in G:
                            G.add_node(path, type="dir", size=0)
                            G.add_edge(parent, path)
                    else:
                        size_str, name = entry.split()
                        size = int(size_str)
                        path = parent.rstrip("/") + "/" + name
                        G.add_node(path, type="file", size=size)
                        G.add_edge(parent, path)
                    i += 1
                continue

            i += 1

        return G

    def dir_size(self, G: nx.DiGraph, node):
        total = 0
        for n in set(nx.descendants(G, node)) | {node}:
            total += G.nodes[n]["size"]
        return total

    def solve(self) -> None:
        G = self.build_fs()

        dir_sizes = {
            node: self.dir_size(G, node)
            for node in G.nodes
            if G.nodes[node]["type"] == "dir"
        }

        self.part1 = sum(size for size in dir_sizes.values() if size <= 100_000)

        total_space = 70_000_000
        needed = 30_000_000
        used = dir_sizes["/"]
        free = total_space - used
        need_more = needed - free
        self.part2 = min(size for size in dir_sizes.values() if size >= need_more)



Day7(2022, 7, InputType.LINES).run()
