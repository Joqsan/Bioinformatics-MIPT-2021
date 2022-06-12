import numpy as np
import pandas as pd
from collections import Counter
from scipy import stats

alphabet = list('ACGT')
letter_to_id = {letter: idx for idx, letter in enumerate(alphabet)}


def most_probable_kmer(text, k, profile_matrix):
    
    """
    output:
        most probable kmer in text for given profile matrix
    """
    
    best_proba = -np.inf
    most_proba_kmer = None
    
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        indexes = [letter_to_id[char] for char in kmer]
        
        string_proba = np.choose(indexes, profile_matrix).prod()
        
        if string_proba > best_proba:
            best_proba = string_proba
            most_proba_kmer = kmer
    
    return np.array(list(most_proba_kmer))


def get_profile_with_pseudocounts(motifs):
    
    """
    input:
        motifs: np.array
    
    output:
        profile matrix
    """
    
    counter = np.apply_along_axis(Counter, 0, motifs)
    counter = [dict(c) for c in counter]
    
    count_motifs = pd.DataFrame(counter, columns=list('ACGT')).fillna(0).T.to_numpy()
    
    # Laplace’s Rule of Succession
    count_motifs = count_motifs + 1
    
    # Plus 4, since for each letter in the alphabet (ACGT) we add 1
    profile = count_motifs / (len(motifs) + 4)
    
    return profile


def get_scores(motifs, t):
    
    """
    input:
        motifs: np.array
    
    output:
        score of given motifs matrix
    """
    
    modes, counts = stats.mode(motifs)
    scores = t - counts
    
    return scores.sum()


def greedy_motif_search_with_pseudocounts(dna, k, t):
    dna_arr = np.array([list(text) for text in dna])
    
    best_motifs = dna_arr[:, :k]
    best_score = get_scores(best_motifs, t)
    
    for i in range(dna_arr.shape[1]-k+1):
        motifs_list = dna_arr[0, i:i+k][np.newaxis] #motif_1
        
        for j in range(1,t):
            profile = get_profile_with_pseudocounts(motifs_list)
            most_proba_kmer = most_probable_kmer(dna[j], k, profile)
            
            motifs_list = np.row_stack([motifs_list, most_proba_kmer])
            
        score_motifs_list = get_scores(motifs_list, t)
        
        if score_motifs_list < best_score:
            best_score = score_motifs_list
            best_motifs = motifs_list.copy()
    
    best_motifs = [''.join(motif_arr.tolist()) for motif_arr in best_motifs]
    
    return best_motifs


def main():
    
    file = open('greedy_motif_search_pseudocounts.txt', 'r')
    
    k, t = list(map(int, next(file).split()))
    
    
    dna = []
    for string in file:
        dna.append(string.strip())
    
    
    print("\n".join(greedy_motif_search_with_pseudocounts(dna, k, t)))

    file.close()


if __name__ == "__main__":
    main()