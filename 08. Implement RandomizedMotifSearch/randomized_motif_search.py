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


def get_motifs_profile_dna(profile, dna, k):
    motifs = []
    for text in dna:
        motifs.append(most_probable_kmer(text, k, profile))
    
    return np.row_stack(motifs)



def randomized_greedy_motif_search(dna, k, t, best_so_far):
    # including pseudocounts
    
    dna_arr = np.array([list(text) for text in dna])
    
    # random index selection
    idxs = np.random.randint(0, dna_arr.shape[1]-k+1, t)[:, None]
    idxs = idxs + np.arange(k)
    
    # use indexes to randomly select the initial motifs
    best_motifs = np.take_along_axis(dna_arr, idxs, axis=1)
    best_score = best_so_far
    
    ## code Motifs(Profile, DNA): https://stepik.org/lesson/240243/step/2?unit=214002
    
    motifs_list = best_motifs.copy()
    while True:
        profile = get_profile_with_pseudocounts(motifs_list)
        motifs_list = get_motifs_profile_dna(profile, dna, k) #Motifs(Profile, Dna)
            
        score_motifs_list = get_scores(motifs_list, t)
        
        if score_motifs_list < best_score:
            best_score = score_motifs_list
            best_motifs = motifs_list.copy()
        else:
            break
            
    
    best_motifs = [''.join(motif_arr.tolist()) for motif_arr in best_motifs]
    
    return best_motifs, best_score



def find_best_approx(dna, k, t, n_times=1000):
    
    best_motifs = None
    best_score = np.inf
    
    curr_score = np.inf
    for i in tqdm(range(n_times)):
        curr_motifs, curr_score = randomized_greedy_motif_search(dna, k, t, curr_score)
        
        if curr_score < best_score:
            best_score = curr_score
            best_motifs = curr_motifs
    
    
    return best_motifs


def main():
    
    file = open('randomized_motif_search.txt', 'r')
    
    k, t = list(map(int, next(file).split()))
    
    print(k, t)
    
    dna = []
    for string in file:
        dna.append(string.strip())
        
    print(dna)
    
    
    print("\n".join(find_best_approx(dna, k, t)))

    file.close()



if __name__ == "__main__":
    main()