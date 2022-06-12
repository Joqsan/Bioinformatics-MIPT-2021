import numpy as np
from collections import defaultdict


def build_path_graph(Adj, paired_reads):
    s = None
    vertices = []
    # degree_balance[v] = in_degree[v] - out_degree[v]
    degree_balance = defaultdict(int)
    for read_1, read_2 in paired_reads:
        prefix = (read_1[:-1], read_2[:-1])
        suffix = (read_1[1:], read_2[1:])
        vertices.extend([prefix, suffix])
        Adj[prefix].append(suffix)
        degree_balance[prefix] -= 1
        degree_balance[suffix] += 1
    degree_balance = np.array([degree_balance[v] for v in vertices])

    # for source in_degree[v] = 0 and out_degree[v] > 0
    # ==> degree_balance[s] < 0
    s = vertices[np.where(degree_balance < 0)[0][0]]
    return s

# DFS to prepare for gluing
def dfs(s, Adj):
    euler = []
    path = [s]
    u = s
    while path:
        if len(Adj[u]):
            path.append(u)
            u = Adj[u].pop()
        else:
            euler.append(u)
            u = path.pop()
    euler.reverse()
    euler = np.vstack(euler)
    
    return euler


def get_string(euler, k, d):
    reads1, reads2 = zip(*euler)
    part1 = reads1[0][:-1] + ''.join([p[-1] for p in reads1])
    part2 = reads2[0][:-1] + ''.join([p[-1] for p in reads2])

    return part1[:k+d] + part2


def string_from_read_pairs(k, d, paired_reads):
    
    Adj = defaultdict(list)
    s = build_path_graph(Adj, paired_reads)
    euler = dfs(s, Adj)
    
    return get_string(euler, k, d)
    
def main():
    
    file = open('rosalind_ba3j.txt', 'r')
    
    k, d = list(map(int, next(file).split()))
    
    paired_reads = []
    for s in file:
        s = s.strip()
        paired_reads.append(s.split('|'))
    
    print(string_from_read_pairs(k, d, paired_reads))

    file.close()
    

if __name__ == '__main__':
    main()