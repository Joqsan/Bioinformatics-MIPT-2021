from collections import defaultdict
import numpy as np


class Graph:
    def __init__(self):
        self.Adj = defaultdict(list)

    def build_graph(self, cycles):
        for cycle in cycles:
            self.create_edge(cycle)

    def create_edge(self, cycle,):
        n = len(cycle)
        for i in range(n):
            j = (i + 1) % n
            u = get_u_in(cycle[j])
            v = get_v_out(cycle[i])
            self.Adj[v].append(u)
            self.Adj[u].append(v)

    def get_two_break_on_graph(self, i1, i2, j1, j2):
        for u, v in [(i1, i2), (i2, i1), (j1, j2), (j2, j1)]:
            self.Adj[u].remove(v)
        for u, v in [(i1, j1), (j1, i1), (i2, j2), (j2, i2)]:
            self.Adj[u].append(v)

    def dfs(self, u, visited, nodes_in_cycle):
        visited.add(u)
        if u % 2 == 0:
            nodes_in_cycle.append(u // 2 + 1)
        else:
            nodes_in_cycle.append(-(u // 2) - 1)
        v = u - 1 if u % 2 else u + 1
        if v not in visited:
            visited.add(v)
            v = self.Adj[v][0]
            if v in visited:
                return
            self.dfs(v, visited, nodes_in_cycle)

    def graph_to_genome(self, n):
        visited = set()
        resulting_genome = []
        for v in range(2 * n):
            if v not in visited:
                nodes_in_cycle = []
                self.dfs(v, visited, nodes_in_cycle)
                resulting_genome.append(nodes_in_cycle)

        result = []
        for nodes_in_cycle in resulting_genome:
            res = [str(u) if u < 0 else '+' + str(u) for u in nodes_in_cycle]
            result.append('(' + ' '.join(res) + ')')

        return ' '.join(result)


def get_u_in(n):
    v = 2 * abs(n) - 2
    if n < 0:
        v += 1
    return v


def get_v_out(n):
    v = 2 * abs(n) - 1
    if n < 0:
        v -= 1
    return v


def main():

    file = open('rosalind_ba6k.txt', 'r')

    genome = next(file).strip()
    indices = np.array(list(map(int, next(file).strip().split(', ')))) - 1

    cycles = [list(map(int, s[:-1].split())) for s in genome.split('(')]
    n = sum(len(cycle) for cycle in cycles)

    graph = Graph()
    graph.build_graph(cycles)
    graph.get_two_break_on_graph(*indices)
    print(graph.graph_to_genome(n))


if __name__ == '__main__':
    main()