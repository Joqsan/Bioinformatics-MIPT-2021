import sys
from collections import defaultdict


def get_genomes(gen):
    gen_list = gen.split(")(")
    gen_list[0] = gen_list[0][1:]
    gen_list[-1] = gen_list[-1][:-1]
    genome = []
    for token in gen_list:
        genome.append(list(map(int, token.split())))
    return genome


def build_breakpoint_graph(genome_1, genome_2):
    Adj = defaultdict(list)

    node_by_block = dict()
    block_by_node = dict()

    n_blocks = 0
    curr_last = -1
    for cycle in genome_1:
        for block in cycle:
            block = abs(block)
            if block not in node_by_block:
                n_blocks += 1
                start = curr_last + 1
                end = curr_last + 2

                node_by_block[block] = (start, end)
                block_by_node[start] = block
                block_by_node[end] = block
                curr_last = end

    concat = genome_1 + genome_2
    for cycle in concat:
        block = abs(cycle[0])

        start, end = node_by_block[block]
        u = end if cycle[0] > 0 else start  # previous node

        cycle = cycle[1:] + [cycle[0]]
        for curr_block in cycle:
            start, end = node_by_block[abs(curr_block)]
            v = start if curr_block > 0 else end  # current node
            Adj[v].append(u)
            Adj[u].append(v)
            u = start if v == end else end

    return n_blocks, Adj


def dfs(u_node, Adj, visited):
    visited.add(u_node)
    for v_node in Adj[u_node]:
        if v_node not in visited:
            dfs(v_node, Adj, visited)


def two_break_distance(genome_1, genome_2):
    num_cycles = 0
    visited = set()
    n_blocks, Adj = build_breakpoint_graph(genome_1, genome_2)
    for u_node in Adj:
        if u_node not in visited:
            dfs(u_node, Adj, visited)
            num_cycles += 1

    # page 321: 2-Break Distance Theorem: The 2-break distance between genomes
    # P and Q is equal to BLOCKS(P, Q) - CYCLES(P, Q).
    return n_blocks - num_cycles


def main():
    sys.setrecursionlimit(int(1e5))

    file = open('rosalind_ba6c.txt', 'r')

    genome_1 = get_genomes(next(file).strip())
    genome_2 = get_genomes(next(file).strip())

    print(two_break_distance(genome_1, genome_2))


if __name__ == '__main__':
    main()