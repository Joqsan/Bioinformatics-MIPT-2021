import numpy as np
from scipy.spatial.distance import hamming


def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    
    distance = 0
    
    pattern = np.array(list(pattern))
    dna = np.array([list(text) for text in dna])
    
    
    for text in dna:
        
        best_hamming = np.inf
        
        for i in range(len(text) - k + 1):
            kmer = text[i:i+k]
            
            curr_hamming = int(np.rint(hamming(pattern, kmer)*k))
            
            if best_hamming > curr_hamming:
                best_hamming = curr_hamming
        
        distance += best_hamming
    
    return distance


def main():
    file = open('rosalind_ba2h.txt', 'r')

    pattern = next(file).strip()

    dna = []
    for string in file:
        dna.append(string.strip())

    print(distance_between_pattern_and_strings(pattern, dna))

    file.close()

if __name__ == "__main__":
    main()