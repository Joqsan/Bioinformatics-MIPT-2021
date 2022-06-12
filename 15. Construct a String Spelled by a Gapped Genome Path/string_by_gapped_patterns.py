
# A modified version of the function get_string
# from problem 13.
def get_string(gapped_patterns, k, d):
    reads1, reads2 = zip(*gapped_patterns)
    prefix_string = reads1[0][:-1] + ''.join([p[-1] for p in reads1])
    suffix_string = reads2[0][:-1] + ''.join([p[-1] for p in reads2])
    
    
    for i in range(k+d+1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return ''

    return prefix_string[:k+d] + suffix_string


def main():
    
    file = open('rosalind_ba3l.txt', 'r')
    
    k, d = list(map(int, next(file).split()))
    
    gapped_patterns = []
    for s in file:
        s = s.strip()
        gapped_patterns.append(s.split('|'))
    
    #print(gapped_patterns)
    
    print(get_string(gapped_patterns, k, d))

    file.close()


if __name__ == '__main__':
    main()