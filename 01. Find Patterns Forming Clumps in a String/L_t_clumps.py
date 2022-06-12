from collections import defaultdict
import numpy as np

def FrequencyTable(text, k):
    freqtable = defaultdict(int)
    
    for i in range(len(text)-k):
        pattern = text[i:i+k]
        
        freqtable[pattern]+=1
    
    return freqtable

def FindClumps(text, k, L, t):
    
    patterns = []
    
    for i in range(len(text)-L):
        window = text[i:i+L]
        freqmap = FrequencyTable(window, k)
        
        for key, freq in freqmap.items():
            if freq >= t:
                patterns.append(key)
    
    return np.unique(patterns).tolist()

def main():
    
    file = open('rosalind_ba1e.txt', 'r')
    
    text = next(file)
    k, L, t = list(map(int, next(file).split()))
    
    print(" ".join(FindClumps(text, k, L, t)))

    file.close()
    
if __name__ == "__main__":
    main()