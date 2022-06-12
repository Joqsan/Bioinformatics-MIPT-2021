from math import inf

scoring_matrix_pam = {
    "A": {"A": 2, "C": -2, "D": 0, "E": 0, "F": -3, "G": 1, "H": -1, "I": -1, "K": -1, "L": -2, "M": -1, "N": 0, "P": 1, "Q": 0, "R": -2, "S": 1, "T": 1, "V": 0, "W": -6, "Y": -3, "-": -5},
    "C": {"A": -2, "C": 12, "D": -5, "E": -5, "F": -4, "G": -3, "H": -3, "I": -2, "K": -5, "L": -6, "M": -5, "N": -4, "P": -3, "Q": -5, "R": -4, "S": 0, "T": -2, "V": -2, "W": -8, "Y": 0, "-": -5},
    "D": {"A": 0, "C": -5, "D": 4, "E": 3, "F": -6, "G": 1, "H": 1, "I": -2, "K": 0, "L": -4, "M": -3, "N": 2, "P": -1, "Q": 2, "R": -1, "S": 0, "T": 0, "V": -2, "W": -7, "Y": -4, "-": -5},
    "E": {"A": 0, "C": -5, "D": 3, "E": 4, "F": -5, "G": 0, "H": 1, "I": -2, "K": 0, "L": -3, "M": -2, "N": 1, "P": -1, "Q": 2, "R": -1, "S": 0, "T": 0, "V": -2, "W": -7, "Y": -4, "-": -5},
    "F": {"A": -3, "C": -4, "D": -6, "E": -5, "F": 9, "G": -5, "H": -2, "I": 1, "K": -5, "L": 2, "M": 0, "N": -3, "P": -5, "Q": -5, "R": -4, "S": -3, "T": -3, "V": -1, "W": 0, "Y": 7, "-": -5},
    "G": {"A": 1, "C": -3, "D": 1, "E": 0, "F": -5, "G": 5, "H": -2, "I": -3, "K": -2, "L": -4, "M": -3, "N": 0, "P": 0, "Q": -1, "R": -3, "S": 1, "T": 0, "V": -1, "W": -7, "Y": -5, "-": -5},
    "H": {"A": -1, "C": -3, "D": 1, "E": 1, "F": -2, "G": -2, "H": 6, "I": -2, "K": 0, "L": -2, "M": -2, "N": 2, "P": 0, "Q": 3, "R": 2, "S": -1, "T": -1, "V": -2, "W": -3, "Y": 0, "-": -5},
    "I": {"A": -1, "C": -2, "D": -2, "E": -2, "F": 1, "G": -3, "H": -2, "I": 5, "K": -2, "L": 2, "M": 2, "N": -2, "P": -2, "Q": -2, "R": -2, "S": -1, "T": 0, "V": 4, "W": -5, "Y": -1, "-": -5},
    "K": {"A": -1, "C": -5, "D": 0, "E": 0, "F": -5, "G": -2, "H": 0, "I": -2, "K": 5, "L": -3, "M": 0, "N": 1, "P": -1, "Q": 1, "R": 3, "S": 0, "T": 0, "V": -2, "W": -3, "Y": -4, "-": -5},
    "L": {"A": -2, "C": -6, "D": -4, "E": -3, "F": 2, "G": -4, "H": -2, "I": 2, "K": -3, "L": 6, "M": 4, "N": -3, "P": -3, "Q": -2, "R": -3, "S": -3, "T": -2, "V": 2, "W": -2, "Y": -1, "-": -5},
    "M": {"A": -1, "C": -5, "D": -3, "E": -2, "F": 0, "G": -3, "H": -2, "I": 2, "K": 0, "L": 4, "M": 6, "N": -2, "P": -2, "Q": -1, "R": 0, "S": -2, "T": -1, "V": 2, "W": -4, "Y": -2, "-": -5},
    "N": {"A": 0, "C": -4, "D": 2, "E": 1, "F": -3, "G": 0, "H": 2, "I": -2, "K": 1, "L": -3, "M": -2, "N": 2, "P": 0, "Q": 1, "R": 0, "S": 1, "T": 0, "V": -2, "W": -4, "Y": -2, "-": -5},
    "P": {"A": 1, "C": -3, "D": -1, "E": -1, "F": -5, "G": 0, "H": 0, "I": -2, "K": -1, "L": -3, "M": -2, "N": 0, "P": 6, "Q": 0, "R": 0, "S": 1, "T": 0, "V": -1, "W": -6, "Y": -5, "-": -5},
    "Q": {"A": 0, "C": -5, "D": 2, "E": 2, "F": -5, "G": -1, "H": 3, "I": -2, "K": 1, "L": -2, "M": -1, "N": 1, "P": 0, "Q": 4, "R": 1, "S": -1, "T": -1, "V": -2, "W": -5, "Y": -4, "-": -5},
    "R": {"A": -2, "C": -4, "D": -1, "E": -1, "F": -4, "G": -3, "H": 2, "I": -2, "K": 3, "L": -3, "M": 0, "N": 0, "P": 0, "Q": 1, "R": 6, "S": 0, "T": -1, "V": -2, "W": 2, "Y": -4, "-": -5},
    "S": {"A": 1, "C": 0, "D": 0, "E": 0, "F": -3, "G": 1, "H": -1, "I": -1, "K": 0, "L": -3, "M": -2, "N": 1, "P": 1, "Q": -1, "R": 0, "S": 2, "T": 1, "V": -1, "W": -2, "Y": -3, "-": -5},
    "T": {"A": 1, "C": -2, "D": 0, "E": 0, "F": -3, "G": 0, "H": -1, "I": 0, "K": 0, "L": -2, "M": -1, "N": 0, "P": 0, "Q": -1, "R": -1, "S": 1, "T": 3, "V": 0, "W": -5, "Y": -3, "-": -5},
    "V": {"A": 0, "C": -2, "D": -2, "E": -2, "F": -1, "G": -1, "H": -2, "I": 4, "K": -2, "L": 2, "M": 2, "N": -2, "P": -1, "Q": -2, "R": -2, "S": -1, "T": 0, "V": 4, "W": -6, "Y": -2, "-": -5},
    "W": {"A": -6, "C": -8, "D": -7, "E": -7, "F": 0, "G": -7, "H": -3, "I": -5, "K": -3, "L": -2, "M": -4, "N": -4, "P": -6, "Q": -5, "R": 2, "S": -2, "T": -5, "V": -6, "W": 17, "Y": 0, "-": -5},
    "Y": {"A": -3, "C": 0, "D": -4, "E": -4, "F": 7, "G": -5, "H": 0, "I": -1, "K": -4, "L": -1, "M": -2, "N": -2, "P": -5, "Q": -4, "R": -4, "S": -3, "T": -3, "V": -2, "W": 0, "Y": 10, "-": -5},
    "-": {"A": -5, "C": -5, "D": -5, "E": -5, "F": -5, "G": -5, "H": -5, "I": -5, "K": -5, "L": -5, "M": -5, "N": -5, "P": -5, "Q": -5, "R": -5, "S": -5, "T": -5, "V": -5, "W": -5, "Y": -5, "-": -100000}
}


# The same as in problem 24, but taking into account the
# "free taxi rides" in the DAG (page 259)
class DpWithBacktracking:
    def __init__(self):
        self.x_prev = None
        self.y_prev = None
        self.val = -inf

    def get_x(self):
        return self.x_prev

    def get_y(self):
        return self.y_prev

    def get_val(self):
        return self.val

    def relax(self, x_prev, y_prev, value):
        if self.val < value:
            self.val = value
            self.x_prev = x_prev
            self.y_prev = y_prev


def highest_scoring_local_alignment(amino_1, amino_2):
    n = len(amino_1)
    m = len(amino_2)

    dp = [[DpWithBacktracking() for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0].relax(None, None, 0)

    for j in range(m):
        dp[0][j + 1].relax(0, j, dp[0][j].get_val() + scoring_matrix_pam['-'][amino_2[j]])
        # checking for free taxi ride
        dp[0][j + 1].relax(None, None, 0)

    for i in range(n):
        dp[i + 1][0].relax(i, 0, dp[i][0].get_val() + scoring_matrix_pam['-'][amino_1[i]])
        # checking for free taxi ride
        dp[i + 1][0].relax(None, None, 0)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j].relax(i, j - 1, dp[i][j - 1].get_val() + scoring_matrix_pam['-'][amino_2[j - 1]])
            dp[i][j].relax(i - 1, j, dp[i - 1][j].get_val() + scoring_matrix_pam[amino_1[i - 1]]['-'])
            dp[i][j].relax(i - 1, j - 1, dp[i - 1][j - 1].get_val() + scoring_matrix_pam[amino_1[i - 1]][amino_2[j - 1]])

            # checking for free taxi ride
            dp[i][j].relax(None, None, 0)

    return dp


def find_end_of_conserved_interval(n, m, dp):
    i, j = n, m

    for start_i in range(n + 1):
        for start_j in range(m + 1):
            if dp[start_i][start_j].get_val() > dp[i][j].get_val():
                i, j = start_i, start_j

    return i, j, dp[i][j].get_val()


def get_alignment(amino_1, amino_2, dp):
    n = len(amino_1)
    m = len(amino_2)

    result_1 = []
    result_2 = []

    # largest_val = dp[m][n]
    i, j, largest_val = find_end_of_conserved_interval(n, m, dp)


    # get alignments (will be in the reverse order, from the end to
    # the beginning).
    while i or j and dp[i][j].get_val() >= 0:
        if dp[i][j].get_x() == i:
            result_1.append('-')
            result_2.append(amino_2[j - 1])
        elif dp[i][j].get_y() == j:
            result_1.append(amino_1[i - 1])
            result_2.append('-')
        else:
            result_1.append(amino_1[i - 1])
            result_2.append(amino_2[j - 1])
        i, j = dp[i][j].get_x(), dp[i][j].get_y()

    # reverse alignments in the correct order
    return largest_val, result_1[::-1][1:], result_2[::-1][1:]


def main():
    
    file = open('rosalind_ba5f.txt', 'r')
    
    amino_1 = next(file).strip()
    amino_2 = next(file).strip()

    dp = highest_scoring_local_alignment(amino_1, amino_2)

    largest_val, result_1, result_2 = get_alignment(amino_1, amino_2, dp)

    print(largest_val)
    print(''.join(result_1))
    print(''.join(result_2))


if __name__ == '__main__':
    main()