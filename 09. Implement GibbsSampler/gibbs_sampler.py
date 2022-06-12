import numpy as np
import pandas as pd
from collections import Counter
from scipy import stats
from tqdm import tqdm

alphabet = list('ACGT')
letter_to_id = {letter: idx for idx, letter in enumerate(alphabet)}


def profile_random_kmer(text, k, profile_matrix):
    """
    output:
        profile-randomly generated kmer in text for given profile matrix
    """

    p = []

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        indexes = [letter_to_id[char] for char in kmer]

        string_proba = np.choose(indexes, profile_matrix).prod()

        p.append(string_proba)

    p = np.array(p) / sum(p)

    start = np.random.choice(a=np.arange(len(text) - k + 1), p=p)
    rand_kmer = text[start:start + k]

    return np.array(list(rand_kmer))


def most_probable_kmer(text, k, profile_matrix):
    """
    output:
        most probable kmer in text for given profile matrix
    """

    best_proba = -np.inf
    most_proba_kmer = None

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
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


def gibbs_sampler(dna, k, t, N):
    # including pseudocounts

    dna_arr = np.array([list(text) for text in dna])

    # random index selection
    idxs = np.random.randint(0, dna_arr.shape[1] - k + 1, t)[:, None]
    idxs = idxs + np.arange(k)

    # use indexes to randomly select the initial motifs
    best_motifs = np.take_along_axis(dna_arr, idxs, axis=1)
    best_score = np.inf

    motifs_list = best_motifs.copy()
    for j in range(N):

        i = np.random.randint(0, t)

        all_motifs_but_i = np.delete(motifs_list, i, axis=0)

        profile = get_profile_with_pseudocounts(all_motifs_but_i)
        motif_i = profile_random_kmer(dna[i], k, profile)

        motifs_list = np.insert(all_motifs_but_i, i, motif_i, axis=0)

        score_motifs_list = get_scores(motifs_list, t)

        if score_motifs_list < best_score:
            best_score = score_motifs_list
            best_motifs = motifs_list.copy()

    best_motifs = [''.join(motif_arr.tolist()) for motif_arr in best_motifs]

    return best_motifs, best_score


def find_best_approx(dna, k, t, N):
    best_motifs = None
    best_score = np.inf

    curr_score = np.inf
    for i in tqdm(range(10)):
        curr_motifs, curr_score = gibbs_sampler(dna, k, t, N)

        if curr_score < best_score:
            best_score = curr_score
            best_motifs = curr_motifs

    return best_motifs


def main():
    file = open('rosalind_ba2g.txt', 'r')

    k, t, N = list(map(int, next(file).split()))

    # print(k, t)

    dna = []
    for string in file:
        dna.append(string.strip())

    # print(dna)

    print("\n".join(find_best_approx(dna, k, t, N)))

    file.close()

if __name__ == "__main__":
    main()