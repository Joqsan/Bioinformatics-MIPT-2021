def hamming(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def approx_matching(pattern, text, d):
    k = len(pattern)
    idxs = []
    
    for i in range(len(text)-k+1):
        substring = text[i:i+k]
        
        if hamming(pattern, substring) <= d:
            idxs.append(i)
    
    return idxs

def main():
    
    file = open('rosalind_ba1h.txt', 'r')
    
    pattern = next(file).strip() #weird that the newline character sticks to the string
    text = next(file).strip()
    d = int(next(file))
    
    result = approx_matching(pattern, text, d)
    
    print(" ".join([str(idx) for idx in result]))

    file.close()

if __name__ == "__main__":
    main()