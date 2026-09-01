class Solution:

    def palindromicStrings(self, n, k):
        MOD = int(1e9 + 7)

        nPr = [[0] * (k + 1) for _ in range(k + 1)]

        for i in range(k + 1):
            for j in range(i + 1):
                # Base Cases
                if j == 0:
                    nPr[i][j] = 1
                else:
                    nPr[i][j] = (nPr[i - 1][j] % MOD +
                                 (j * nPr[i - 1][j - 1]) % MOD) % MOD

        ans = 0

        for i in range(1, n // 2 + 1):
            ans = (ans + nPr[k][i]) % MOD

        ans = (ans * 2) % MOD

        if n % 2 == 1:
            ans = (ans + nPr[k][n // 2 + 1]) % MOD

        return int(ans)