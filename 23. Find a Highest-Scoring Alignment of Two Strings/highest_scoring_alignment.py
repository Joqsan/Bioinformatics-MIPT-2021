from math import inf

scoring_matrix = {
    "A": {"A": 4, "C": 0, "D": -2, "E": -1, "F": -2, "G": 0, "H": -2, "I": -1, "K": -1, "L": -1, "M": -1, "N": -2, "P": -1, "Q": -1, "R": -1, "S": 1, "T": 0, "V": 0, "W": -3, "Y": -2, "-": -5},
    "C": {"A": 0, "C": 9, "D": -3, "E": -4, "F": -2, "G": -3, "H": -3, "I": -1, "K": -3, "L": -1, "M": -1, "N": -3, "P": -3, "Q": -3, "R": -3, "S": -1, "T": -1, "V": -1, "W": -2, "Y": -2, "-": -5},
    "D": {"A": -2, "C": -3, "D": 6, "E": 2, "F": -3, "G": -1, "H": -1, "I": -3, "K": -1, "L": -4, "M": -3, "N": 1, "P": -1, "Q": 0, "R": -2, "S": 0, "T": -1, "V": -3, "W": -4, "Y": -3, "-": -5},
    "E": {"A": -1, "C": -4, "D": 2, "E": 5, "F": -3, "G": -2, "H": 0, "I": -3, "K": 1, "L": -3, "M": -2, "N": 0, "P": -1, "Q": 2, "R": 0, "S": 0, "T": -1, "V": -2, "W": -3, "Y": -2, "-": -5},
    "F": {"A": -2, "C": -2, "D": -3, "E": -3, "F": 6, "G": -3, "H": -1, "I": 0, "K": -3, "L": 0, "M": 0, "N": -3, "P": -4, "Q": -3, "R": -3, "S": -2, "T": -2, "V": -1, "W": 1, "Y": 3, "-": -5},
    "G": {"A": 0, "C": -3, "D": -1, "E": -2, "F": -3, "G": 6, "H": -2, "I": -4, "K": -2, "L": -4, "M": -3, "N": 0, "P": -2, "Q": -2, "R": -2, "S": 0, "T": -2, "V": -3, "W": -2, "Y": -3, "-": -5},
    "H": {"A": -2, "C": -3, "D": -1, "E": 0, "F": -1, "G": -2, "H": 8, "I": -3, "K": -1, "L": -3, "M": -2, "N": 1, "P": -2, "Q": 0, "R": 0, "S": -1, "T": -2, "V": -3, "W": -2, "Y": 2, "-": -5},
    "I": {"A": -1, "C": -1, "D": -3, "E": -3, "F": 0, "G": -4, "H": -3, "I": 4, "K": -3, "L": 2, "M": 1, "N": -3, "P": -3, "Q": -3, "R": -3, "S": -2, "T": -1, "V": 3, "W": -3, "Y": -1, "-": -5},
    "K": {"A": -1, "C": -3, "D": -1, "E": 1, "F": -3, "G": -2, "H": -1, "I": -3, "K": 5, "L": -2, "M": -1, "N": 0, "P": -1, "Q": 1, "R": 2, "S": 0, "T": -1, "V": -2, "W": -3, "Y": -2, "-": -5},
    "L": {"A": -1, "C": -1, "D": -4, "E": -3, "F": 0, "G": -4, "H": -3, "I": 2, "K": -2, "L": 4, "M": 2, "N": -3, "P": -3, "Q": -2, "R": -2, "S": -2, "T": -1, "V": 1, "W": -2, "Y": -1, "-": -5},
    "M": {"A": -1, "C": -1, "D": -3, "E": -2, "F": 0, "G": -3, "H": -2, "I": 1, "K": -1, "L": 2, "M": 5, "N": -2, "P": -2, "Q": 0, "R": -1, "S": -1, "T": -1, "V": 1, "W": -1, "Y": -1, "-": -5},
    "N": {"A": -2, "C": -3, "D": 1, "E": 0, "F": -3, "G": 0, "H": 1, "I": -3, "K": 0, "L": -3, "M": -2, "N": 6, "P": -2, "Q": 0, "R": 0, "S": 1, "T": 0, "V": -3, "W": -4, "Y": -2, "-": -5},
    "P": {"A": -1, "C": -3, "D": -1, "E": -1, "F": -4, "G": -2, "H": -2, "I": -3, "K": -1, "L": -3, "M": -2, "N": -2, "P": 7, "Q": -1, "R": -2, "S": -1, "T": -1, "V": -2, "W": -4, "Y": -3, "-": -5},
    "Q": {"A": -1, "C": -3, "D": 0, "E": 2, "F": -3, "G": -2, "H": 0, "I": -3, "K": 1, "L": -2, "M": 0, "N": 0, "P": -1, "Q": 5, "R": 1, "S": 0, "T": -1, "V": -2, "W": -2, "Y": -1, "-": -5},
    "R": {"A": -1, "C": -3, "D": -2, "E": 0, "F": -3, "G": -2, "H": 0, "I": -3, "K": 2, "L": -2, "M": -1, "N": 0, "P": -2, "Q": 1, "R": 5, "S": -1, "T": -1, "V": -3, "W": -3, "Y": -2, "-": -5},
    "S": {"A": 1, "C": -1, "D": 0, "E": 0, "F": -2, "G": 0, "H": -1, "I": -2, "K": 0, "L": -2, "M": -1, "N": 1, "P": -1, "Q": 0, "R": -1, "S": 4, "T": 1, "V": -2, "W": -3, "Y": -2, "-": -5},
    "T": {"A": 0, "C": -1, "D": -1, "E": -1, "F": -2, "G": -2, "H": -2, "I": -1, "K": -1, "L": -1, "M": -1, "N": 0, "P": -1, "Q": -1, "R": -1, "S": 1, "T": 5, "V": 0, "W": -2, "Y": -2, "-": -5},
    "V": {"A": 0, "C": -1, "D": -3, "E": -2, "F": -1, "G": -3, "H": -3, "I": 3, "K": -2, "L": 1, "M": 1, "N": -3, "P": -2, "Q": -2, "R": -3, "S": -2, "T": 0, "V": 4, "W": -3, "Y": -1, "-": -5},
    "W": {"A": -3, "C": -2, "D": -4, "E": -3, "F": 1, "G": -2, "H": -2, "I": -3, "K": -3, "L": -2, "M": -1, "N": -4, "P": -4, "Q": -2, "R": -3, "S": -3, "T": -2, "V": -3, "W": 11, "Y": 2, "-": -5},
    "Y": {"A": -2, "C": -2, "D": -3, "E": -2, "F": 3, "G": -3, "H": 2, "I": -1, "K": -2, "L": -1, "M": -1, "N": -2, "P": -3, "Q": -1, "R": -2, "S": -2, "T": -2, "V": -1, "W": 2, "Y": 7, "-": -5},
    "-": {"A": -5, "C": -5, "D": -5, "E": -5, "F": -5, "G": -5, "H": -5, "I": -5, "K": -5, "L": -5, "M": -5, "N": -5, "P": -5, "Q": -5, "R": -5, "S": -5, "T": -5, "V": -5, "W": -5, "Y": -5, "-": -10000000}
}


# Similar to problem 22, but we create a class so that for each cell (i, j)
# we keep track of the current longest path to (i, j) (the maximum aggregated
# scoring for alignment (amino_1[i], -), (-, amino_2[j]) and (amino_1[i], amino_2[j]))
# and the corresponding indices for backtracking (strictly speaking, it's not
# backtracking, but keeping track of the predecessor cell of (i, j)).
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


def highest_scoring_alignment(amino_1, amino_2):
    n = len(amino_1)
    m = len(amino_2)

    dp = [[DpWithBacktracking() for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0].relax(None, None, 0)

    for j in range(m):
        dp[0][j + 1].relax(0, j, dp[0][j].get_val() + scoring_matrix['-'][amino_2[j]])

    for i in range(n):
        dp[i + 1][0].relax(i, 0, dp[i][0].get_val() + scoring_matrix['-'][amino_1[i]])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j].relax(i, j - 1, dp[i][j - 1].get_val() + scoring_matrix['-'][amino_2[j - 1]])
            dp[i][j].relax(i - 1, j, dp[i - 1][j].get_val() + scoring_matrix[amino_1[i - 1]]['-'])
            dp[i][j].relax(i - 1, j - 1, dp[i - 1][j - 1].get_val() + scoring_matrix[amino_1[i - 1]][amino_2[j - 1]])

    return dp


def get_alignment(amino_1, amino_2, dp):
    n = len(amino_1)
    m = len(amino_2)

    result_1 = []
    result_2 = []
    i, j = n, m

    # get alignments (will be in the reverse order, from the end to
    # the beginning).
    while i > 0 or j > 0:
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
    return result_1[::-1], result_2[::-1]


def main():
    
    file = open('rosalind_ba5e.txt', 'r')
    
    amino_1 = next(file).strip()
    amino_2 = next(file).strip()

    dp = highest_scoring_alignment(amino_1, amino_2)

    result_1, result_2 = get_alignment(amino_1, amino_2, dp)

    print(dp[-1][-1].get_val())
    print(''.join(result_1))
    print(''.join(result_2))


if __name__ == '__main__':
    main()