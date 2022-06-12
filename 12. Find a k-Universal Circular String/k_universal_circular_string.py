def k_universal_circular(k):
    edges = ['1' for _ in range(k)]
    visited = {''.join(edges)}
    
    # instead of counting the number of connected components
    # we count the # of edges (k-binary strings) already joined
    # minus k to ignore the row of 1's at the end
    for i in range((1 << k) - k):
        pattern = ''.join(edges[-k + 1:] + ['0'])
        if pattern in visited:
            edges.append('1')
        else:
            edges.append('0')
        visited.add(''.join(edges[-k:]))

    return ''.join(edges)


def main():
    
    file = open('rosalind_ba3i.txt', 'r')
    
    k = int(next(file))
    
    print(k_universal_circular(k))

    file.close()

    
if __name__ == '__main__':
    main()