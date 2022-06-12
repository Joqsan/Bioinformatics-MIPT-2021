import numpy as np
import itertools as it
from collections import defaultdict

alphabet = list('ATGC')
def d_mismatch_generator(pattern, d):
    k = len(pattern)
    
    idx_picked = it.combinations(range(k), r=d)
    letters_picked = it.product(alphabet, repeat=d)
    
    pairs = it.product(idx_picked, letters_picked)
    
    base_pattern = np.array(list(pattern))
    
    d_mismatches = []
    for idxs, letters in pairs:
        temp = base_pattern.copy()
        
        temp[list(idxs)] = letters
        
        
        d_mismatches.append(''.join(temp))
    
    return d_mismatches

def get_mismatches(pattern, d):
    
    mismatch_list = []
    for k in range(1, d+1):
        mismatch_list += d_mismatch_generator(pattern, k)
    
    return np.unique(mismatch_list).tolist()

def most_freq_mismatches(text, k, d):
    
    freqmap = defaultdict(int)
    max_count = 0
    pattern_list = []
    
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        
        mismatch_list = get_mismatches(pattern, d)
        
        for kmer in mismatch_list:
            freqmap[kmer]+=1
            
            max_count = max(max_count, freqmap[kmer])
    
    for pattern, count in freqmap.items():
        if count == max_count:
            pattern_list.append(pattern)
        
    return pattern_list

def main():
    
    file = open('rosalind_ba1i.txt', 'r')
    
    text = next(file).strip()
    k, d = list(map(int, next(file).split()))
    
    print(" ".join(most_freq_mismatches(text, k, d)))

    file.close()

if __name__ == "__main__":
    main()