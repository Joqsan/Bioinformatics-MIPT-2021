import numpy as np
from collections import defaultdict


def build_graph(Adj, patterns, in_degree, out_degree):
    
    vertices = []
    
    for kmer in patterns:
        prefix, suffix = kmer[:-1], kmer[1:]
        Adj[prefix].append(suffix)

        out_degree[prefix] += 1
        in_degree[suffix] += 1

        vertices.extend([prefix, suffix])

    non_branching = {v: in_degree[v] == 1 and out_degree[v] == 1 for v in vertices}

    return vertices, non_branching


def check_cycles(contigs, visited, vertices, in_degree, out_degree):

    for u in vertices:
        if visited[u] > 0:
            continue
            
        assert in_degree[u] == 1 and out_degree[u] == 1
        visited[u] = True
        cycle = [u]
        v = u
        while True:
            v = Adj[v][0]

            # every vertex in the cycle has to be balanced
            assert in_degree[v] == 1 and out_degree[v] == 1, print(u, v)
            visited[v] = True
            if v == u:
                break
            cycle.append(v[-1])
        contigs.add(''.join(cycle))


def find_contigs(Adj, non_branching, vertices, in_degree, out_degree):
    contigs = set()
    visited = defaultdict(int)
    for u in vertices:
        # if in_degree[u] != out_degree[u], then
        # u is the beginning/end of a contig
        if not non_branching[u]:
            visited[u] = True

            # we check for a non-branching path
            # if u is the beginning
            if out_degree[u] > 0:
                for w in Adj[u]:

                    # build non-branching path
                    path = [u, w[-1]]
                    v = w

                    # Along the path with DFS
                    while non_branching[v]:
                        visited[v] = True
                        v = Adj[v][0]
                        path.append(v[-1])

                    contigs.add(''.join(path))

    check_cycles(contigs, visited, vertices, in_degree, out_degree)

    return '\n'.join(sorted(contigs))
    

def contigs_generation(patterns):
    
    Adj = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    vertices, non_branching = build_graph(Adj, patterns, in_degree, out_degree)
    
    return find_contigs(Adj, non_branching, vertices, in_degree, out_degree)
    

def main():
    
    file = open('rosalind_ba3k.txt', 'r')
    
    patterns = []
    for s in file:
        patterns.append(s.strip())
    
    
    print(contigs_generation(patterns))

    file.close()
    

if __name__ == '__main__':
    main()