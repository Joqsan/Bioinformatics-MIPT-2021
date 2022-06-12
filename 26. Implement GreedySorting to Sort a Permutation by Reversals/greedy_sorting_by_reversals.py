def greedy_sorting_by_reversals(seq):
    result = []

    for k in range(len(seq)):
        if abs(seq[k]) != (k + 1):
            for j in range(k, len(seq)):
                if abs(seq[j]) == (k + 1):
                    seq[k], seq[j] = -seq[j], -seq[k]

                    for i in range(k + 1, j):
                        seq[i] *= -1
                    if j - k > 1:
                        seq[k + 1:j] = seq[k + 1: j][::-1]

            result.append(seq.copy())
        if seq[k] == -(k + 1):
            seq[k] = k + 1

            result.append(seq.copy())

    for permutation in result:
        res = [str(i) if i < 0 else '+' + str(i) for i in permutation]
        print('(' + ' '.join(res) + ')')


def main():
    file = open('rosalind_ba6a.txt', 'r')
    seq = next(file).strip()
    seq = seq[1:-1].split()
    seq = list(map(int, seq))

    greedy_sorting_by_reversals(seq)


if __name__ == '__main__':
    main()