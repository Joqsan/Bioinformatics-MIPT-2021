"""
Idea: Convert target peptide to all possible DNA strings it may have been translated from,
and run a string searching algorithm between each string in this list and the original DNA input.

- (We can convert the peptide to RNA by replacing T by U)
- We could have used a codon_to_amino dict also, and map every codon in Text to Peptide (for each of the 3 starting
    positions).
"""

amino_to_codon = {
    'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'C': ['TGT', 'TGC'],
    'D': ['GAT', 'GAC'],
    'E': ['GAA', 'GAG'],
    'F': ['TTT', 'TTC'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG'],
    'H': ['CAT', 'CAC'],
    'I': ['ATT', 'ATC', 'ATA'],
    'K': ['AAA', 'AAG'],
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'M': ['ATG'],
    'N': ['AAT', 'AAC'],
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'W': ['TGG'],
    'Y': ['TAT', 'TAC']
}


def peptide_to_dna(protein: str) -> list:
    encoding_list = [''] # empty string to allow concatenation
    for amino in protein:
        codon_list = amino_to_codon[amino] # list of encodings for amino
        new_encoding_list = []
        for curr_dna in encoding_list:
            for next_codon in codon_list:
                new_encoding_list.append(curr_dna + next_codon)
        encoding_list = new_encoding_list
    return encoding_list


tab_input = 'ATGC'
tab_output = 'TACG'
trans_tab = str.maketrans(tab_input, tab_output)
def reverse_complement(pattern):
    return pattern[::-1].translate(trans_tab)


def find_encoding_subtrings(dna: str, peptide: str) -> list:
    n = len(dna)
    k = 3 * len(peptide)

    encoding_sequences = set(peptide_to_dna(peptide)) # list to set to allow for O(1) searching

    result = []
    for i in range(n - k + 1):

        dna_substring = dna[i:i + k]
        rc_dna_substring = reverse_complement(dna_substring)

        if dna_substring in encoding_sequences or rc_dna_substring in encoding_sequences:
            result.append(dna_substring)

    return '\n'.join(result)


def main():
    
    file = open('rosalind_ba4b.txt', 'r')
    
    
    dna = next(file).strip()
    peptide = next(file).strip()
    print(find_encoding_subtrings(dna, peptide))


if __name__ == '__main__':
   main()