import numpy as np


def highest_scoring_multiple_alignment(amino_1, amino_2, amino_3):

    n, m, l = len(amino_1), len(amino_2), len(amino_3)
    sizes = np.array([n, m, l])

    dp = np.zeros(shape=sizes+1)
    match_count = np.zeros(shape=sizes+1)

    for j in range(1, m + 1):
        for k in range(1, l + 1):
            match_count[0][j][k] = 1

    for i in range(1, n + 1):
        for k in range(1, l + 1):
            match_count[i][0][k] = 2

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_count[i][j][0] = 3

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if amino_1[i - 1] == amino_2[j - 1] and amino_2[j - 1] == amino_3[k - 1]:
                    match_count[i][j][k] = 4
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    relax(i, j, k, dp, match_count)

    max_score = str(int(dp[n][m][l]))

    result_1, result_2, result_3 = get_multiple_alignment(amino_1, amino_2, amino_3, match_count, sizes)

    print('\n'.join([max_score, result_1, result_2, result_3]))


def get_multiple_alignment(amino_1, amino_2, amino_3, match_count, sizes):

    n, m, l = len(amino_1), len(amino_2), len(amino_3)

    align_1, align_2, align_3 = get_alignment_path(n, m, l, match_count)

    result_1, result_2, result_3 = "", "", ""
    cur_idx = [0, 0, 0]  # [i, j, k]
    string_shift = [align_1[0], align_2[0], align_3[0]]
    max_shift = np.max(string_shift)
    for pos in range(len(align_1)):
        if pos > 0:
            string_shift = [align_1[pos] - align_1[pos - 1], align_2[pos] - align_2[pos - 1],
                            align_3[pos] - align_3[pos - 1]]
            max_shift = np.max(string_shift)

        cur_idx[0], result_1 = append_symbol(amino_1, result_1, cur_idx[0], pos, max_shift, string_shift[0])
        cur_idx[1], result_2 = append_symbol(amino_2, result_2, cur_idx[1], pos, max_shift, string_shift[1])
        cur_idx[2], result_3 = append_symbol(amino_3, result_3, cur_idx[2], pos, max_shift, string_shift[2])

    remaining_shift = sizes - cur_idx
    remaining_max_shift = np.max(remaining_shift)

    result_1 = append_to_end(amino_1, result_1, cur_idx[0], remaining_max_shift, remaining_shift[0])
    result_2 = append_to_end(amino_2, result_2, cur_idx[1], remaining_max_shift, remaining_shift[1])
    result_3 = append_to_end(amino_3, result_3, cur_idx[2], remaining_max_shift, remaining_shift[2])
    return result_1, result_2, result_3


def append_to_end(amino, result, cur_idx, remaining_max_shift, remaining_shift):
    for i in range(remaining_shift):
        result += amino[cur_idx]
        cur_idx += 1
    for i in range(remaining_max_shift - remaining_shift):
        result += "-"
    return result


def append_symbol(amino, result, cur_idx, pos, max_shift, string_shift):
    for i in range(max_shift - string_shift):
        result += '-'
    if pos == 0:
        result += amino[cur_idx]
        cur_idx += 1
    for i in range(string_shift):
        result += amino[cur_idx]
        cur_idx += 1
    return cur_idx, result


def get_alignment_path(n, m, l, match_count):
    i, j, k = n, m, l
    index_path = []
    match_count_path = []
    while i > 0 or j > 0 or k > 0:
        index_path.append([i, j, k])
        if match_count[i][j][k] == 4:
            i -= 1
            j -= 1
            k -= 1
            match_count_path.append(4)
        else:
            if match_count[i][j][k] == 3 and k > 0:
                k -= 1
                match_count_path.append(3)
            else:
                if match_count[i][j][k] == 2 and j > 0:
                    j -= 1
                    match_count_path.append(2)
                else:
                    if match_count[i][j][k] == 1 and i > 0:
                        i -= 1
                        match_count_path.append(1)
                    else:
                        break
    index_path = index_path[::-1]
    match_count_path = match_count_path[::-1]

    alignments_1 = []
    alignments_2 = []
    alignments_3 = []
    for elem in range(len(match_count_path)):
        i, j, k = index_path[elem]
        f = match_count_path[elem]

        # when indexes are aligned
        if f == 4:
            alignments_1.append(i)
            alignments_2.append(j)
            alignments_3.append(k)

    return alignments_1, alignments_2, alignments_3


def relax(i, j, k, dp, pred):

    dp[i][j][k] = np.max([0, dp[i][j][k - 1], dp[i][j - 1][k], dp[i - 1][j][k]])

    if dp[i][j][k] == dp[i - 1][j][k]:
        pred[i][j][k] = 1
    elif dp[i][j][k] == dp[i][j - 1][k]:
        pred[i][j][k] = 2
    else:
        pred[i][j][k] = 3


def main():
    
    file = open('rosalind_ba5m.txt', 'r')
    
    amino_1 = next(file).strip()
    amino_2 = next(file).strip()
    amino_3 = next(file).strip()
    highest_scoring_multiple_alignment(amino_1, amino_2, amino_3)


if __name__ == '__main__':
    main()