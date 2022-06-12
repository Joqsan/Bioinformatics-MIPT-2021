def build_graph(patterns, k, vertices):
    n = len(vertices)
    Adj = [[] for _ in range(n)]
    for kmer in patterns:
        prefix = vertices[kmer[:k - 1]]
        suffix = vertices[kmer[1:]]
        Adj[prefix].append(suffix)
    return Adj


# Find contigs by max non-branching path
def find_max_nonbranching_paths(Adj):
    n = len(Adj)
    in_degree = [0 for _ in range(n)]
    for out_edges in Adj:
        for u in out_edges:
            in_degree[u] += 1
    out_degree = [len(out_edges) for out_edges in Adj]

    non_branching_paths = []
    for u in range(n):
        if in_degree[u] == 1 and out_degree[u] == 1:
            continue
        if out_degree[u] == 0:
            continue
        for v in Adj[u]:
            path = [u, v]
            w = v
            while in_degree[w] == 1 and out_degree[w] == 1:
                w = Adj[w][0]
                path.append(w)
                if len(path) == n: # cycle encountered
                    break
            non_branching_paths.append(path)
    return non_branching_paths


def find_contigs(patterns):
    k = len(patterns[0])
    vertices = get_vertex_set(patterns, k)
    id_to_vertex = {i: v for v, i in vertices.items()}
    Adj = build_graph(patterns, k, vertices)
    non_branching_paths = find_max_nonbranching_paths(Adj)

    contigs = []
    for path in non_branching_paths:
        contig = id_to_vertex[path[0]] + ''.join([id_to_vertex[v][-1] for v in path[1:]])
        contigs.append(contig)

    return contigs


def get_vertex_set(patterns, k):
    # V = (all prefixes) U (all suffixes)
    V = {kmer[:k - 1] for kmer in patterns} | {kmer[1:] for kmer in patterns}
    return {v: i for i, v in enumerate(V)}


def main():
    
    file = open('rosalind_ba3k.txt', 'r')
    
    patterns = []
    for s in file:
        patterns.append(s.strip())
    
    
    print(*find_contigs(patterns))

    file.close()

    
if __name__ == '__main__':
    main()