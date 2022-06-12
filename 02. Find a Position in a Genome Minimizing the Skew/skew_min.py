import numpy as np

# From now onward let's follow PEP8 name convention
def skew_min(genome):
    
    skew_val = [0]
    
    c_counter = 0
    g_counter = 0
    min_val = np.inf # for finding argmin(Skew(Prefix(genome)))
    argmin_skew = []
    
    for i, char in enumerate(genome):
        if char == 'C':
            c_counter += 1
        elif char == 'G':
            g_counter += 1
        
        # current skew
        curr_skew = g_counter - c_counter
        
        # for the current i find argmin(Skew(Prefix(genome)))
        if curr_skew < min_val:
            argmin_skew = []
            argmin_skew.append(i+1)
            min_val = curr_skew
        elif curr_skew == min_val:
            argmin_skew.append(i+1)
    
    return argmin_skew

def main():
    
    file = open('rosalind_ba1f.txt', 'r')
    
    genome = next(file)
    argmin_skew = skew_min(genome)
    #print(skew_min(genome))
    
    print(" ".join([str(idx) for idx in argmin_skew]))

    file.close()

if __name__ == "__main__":
    main()