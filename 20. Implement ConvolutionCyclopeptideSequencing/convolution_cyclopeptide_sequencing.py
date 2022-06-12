import numpy as np


def expand(peptides, alphabet):

    expanded_peptides = []
    for k in range(len(peptides)):
        for i in range(len(alphabet)):
            cur_pep = []

            for t in range(len(peptides[k])):
                cur_pep.append(peptides[k][t])

            cur_pep.append(alphabet[i])
            expanded_peptides.append(cur_pep)
    return expanded_peptides


def mass(peptide):
    return np.sum(peptide)


def theoretical_spectrum(peptide):
    result = [0]

    double_peptide = peptide + peptide

    for k in range(1, len(peptide)):
        for i in range(len(peptide)):
            curr_subpeptide = sum(double_peptide[i : i + k])
            result.append(curr_subpeptide)

    result.append(np.sum(peptide))
    return result


def score(peptide, spectrum):
    if len(peptide) == 0:
        return len(spectrum)

    subpeptides_set = theoretical_spectrum(peptide)

    temp_spectrum = spectrum.copy()

    curr_score = 0
    for elem in subpeptides_set:
        if elem in temp_spectrum:
            temp_spectrum.remove(elem)
            curr_score += 1

    return curr_score


def trim(leaderboard, spec, n):
    if len(leaderboard) <= n:
        return leaderboard

    sorted_leaders = sorted(leaderboard, key=lambda p: score(p, spec))
    trimmed_leaderboard = sorted_leaders[len(sorted_leaders) - n:]

    return trimmed_leaderboard


def find_amino_alphabet(m, spectrum):
    differences = []
    for i in range(len(spectrum) - 1):
        for j in range(i+1, len(spectrum)):
            differences.append(int((np.abs(spectrum[i] - spectrum[j]))))

    alphabet = []

    for peptide in spectrum:
        if peptide >= 57 and peptide <= 200:
            alphabet.append(peptide)

    for peptide in differences:
        if peptide >= 57 and peptide <= 200:
            alphabet.append(peptide)

    alphabet_counts = np.zeros(201)
    for peptide in alphabet:
        alphabet_counts[peptide] += 1

    unique_sorted_alphabet = sorted(np.unique(alphabet), key=lambda k: alphabet_counts[k])
    if len(unique_sorted_alphabet) > m:
        unique_sorted_alphabet = unique_sorted_alphabet[len(unique_sorted_alphabet) - m:]

    return unique_sorted_alphabet


def leaderboard_cyclopeptide_sequencing(spectrum, n, alphabet):
    leaderboard = [[]]
    leader = []
    leader_score = 1

    parent_mass = max(spectrum)

    while len(leaderboard):

        leaderboard = expand(leaderboard, alphabet)
        next_leaderboard = leaderboard.copy()

        for peptide in leaderboard:
            if mass(peptide) == parent_mass:
                curr_score = score(peptide, spectrum)
                if curr_score > leader_score:
                    leader = peptide
                    leader_score = curr_score
            elif mass(peptide) > parent_mass:
                next_leaderboard.remove(peptide)

        leaderboard = trim(next_leaderboard, spectrum, n)

    return '-'.join([str(n) for n in leader])


def convolution_cyclopeptide_sequencing(m, n, spectrum):
    alphabet = find_amino_alphabet(m, spectrum)
    return leaderboard_cyclopeptide_sequencing(spectrum, n, alphabet)


def main():
    file = open('rosalind_ba4i.txt', 'r')
    
    m = int(next(file))
    n = int(next(file))
    spectrum = [int(s) for s in next(file).strip().split()]
    
    print(convolution_cyclopeptide_sequencing(m, n, spectrum))
    

if __name__ == "__main__":
    main()