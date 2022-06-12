
"""
Idea: BnB algorithm in pages 195-196.
"""

amino_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115,128, 129, 131, 137, 147, 156, 163, 186]


def expand(peptides):
    new_peptides = set()
    for peptide in peptides:
        for amino_acid_mass in amino_masses:
            new_peptides.add(peptide + (amino_acid_mass,))
    return new_peptides


def theoretical_spectrum(peptide):
    spectrum = [0]
    spectrum.append(sum(peptide))

    double_peptide = peptide + peptide
    peptide_length = len(peptide)
    for k in range(peptide_length):
        for i in range(1, peptide_length):
            spectrum.append(sum(double_peptide[k: k + i]))

    return sorted(spectrum)


def consistent(peptide, spectrum):

    spectrum_set = set(spectrum)

    for k in range(len(peptide)):
        for i in range(1, len(peptide) + 1):
            if sum(peptide[k:k + i]) not in spectrum_set:
                return False

    return True


def mass(peptide):
    return sum(peptide)


def cyclopeptide_sequencing(spectrum):

    peptides = set([()])
    parent_mass = max(spectrum)
    result = []

    while peptides:
        peptides = expand(peptides)
        old_peptides = peptides.copy()

        for peptide in old_peptides:

            cyclo_spectrum = theoretical_spectrum(peptide)

            if mass(peptide) == parent_mass:
                if cyclo_spectrum == spectrum:
                    result.append('-'.join([str(m) for m in peptide]))
                peptides.remove(peptide)
            elif not consistent(peptide, spectrum):
                peptides.remove(peptide)

    return '\n'.join(result)


def main():
    spectrum = list(map(int, next(open("rosalind_ba4e.txt", "r")).split()))
    print(cyclopeptide_sequencing(spectrum))


if __name__ == "__main__":
    main()