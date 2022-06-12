import numpy as np

amino_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def expand(peptides):
    expanded_peptides = []

    for k in range(len(peptides)):
        for i in range(len(amino_masses)):
            cur_pep = []

            for t in range(len(peptides[k])):
                cur_pep.append(peptides[k][t])

            cur_pep.append(amino_masses[i])
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


def leaderboard_cyclopeptide_sequencing(spectrum, n):
    leaderboard = [[]]
    leader = []
    leader_score = 1

    parent_mass = max(spectrum)

    while len(leaderboard):

        leaderboard = expand(leaderboard)
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


def main():
    file = open('rosalind_ba4g.txt', 'r')

    n = int(next(file))
    spectrum = [int(s) for s in next(file).strip().split()]
    
    print(leaderboard_cyclopeptide_sequencing(spectrum, n))


if __name__ == "__main__":
    main()