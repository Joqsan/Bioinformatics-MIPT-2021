"""
Idea: DP solution. Problem equivalent to the coin problem: finding in how many ways we can add to mass 
having coins with values in amino_masses, where mass \in [0, m]
"""


# page 190
aminoacid_masses = [
    57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186
]


def count_peptides_by_mass(m):
    
    dp = [0 for _ in range(m + 1)]
    dp[0] = 1 # there is just 1 way to add to mass = 0: using no coins.
    for mass in range(m + 1):
        for c in aminoacid_masses:
            if c > mass:
                break
            dp[mass] += dp[mass - c]

    return dp[m]


def main():
    
    file = open('rosalind_ba4d.txt', 'r')
    
    m = int(next(file))
    print(count_peptides_by_mass(m))


if __name__ == '__main__':
   main()