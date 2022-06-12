import numpy as np


# page 306: If pi+1 - pi != 1,then we say that (pi pi+1) is a breakpoint.
def main():
    file = open('rosalind_ba6b.txt', 'r')
    seq = next(file).strip()
    seq = seq[1:-1].split()
    seq = list(map(int, seq))

    breakpoint_count = np.sum(np.diff(seq) != 1)

    if seq[0] != 1:
        breakpoint_count += 1
    if seq[-1] != len(seq):
        breakpoint_count += 1

    print(breakpoint_count)


if __name__ == '__main__':
    main()