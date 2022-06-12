"""
Goal:
- Find Eulerian path in de Bruijn graph (a graph of kmers' prefixes/suffixes)
- (In an Eulerian path all nodes have degree 2 (in_degree = out_degre), except 2 nodes).

Idea: 
- Use a union-find approach, reducing the number of sets from len(kmers) to 1.
    - "Construct" de Bruijn graph on the fly, just by retrieving the current kmer's prefix/suffix.
    - Find: while "building" the graph, check the place in the current target string the current prefix/suffix has.
    - Union: when the prefix/suffix of current node matches the suffix/prefix of the current target string.
"""


def str_from_kmer_composition(k, kmers):

    # lexicographical sorting
    kmers = sorted(kmers)

    # initialization
    target_string = kmers[0]

    # while we don't have just one set.
    while len(kmers) > 1:
        for i, kmer in enumerate(kmers):
            target_len = len(target_string)
            
            # suffix(curr_kmer) == prefix(target)
            if kmer[1:] == target_string[:k-1]:
                target_string = kmer[0] + target_string
            # prefix(curr_kmer) == suffix(target)
            elif kmer[:-1] == target_string[-k+1:]:
                target_string += kmer[-1]

            # if we added the current kmer's preffix/suffix, then unite
            if target_len != len(target_string):
                kmers.pop(i)
                break

    return target_string


def main():
    
    file = open('rosalind_ba3h.txt.txt', 'r')
    
    k = int(next(file))
    
    kmers = []
    for kmer in file:
        kmers.append(kmer.strip())
        
    #print(k)
    #print(kmers)
    
    print(str_from_kmer_composition(k, kmers))

    file.close()


if __name__ == '__main__':
    main()