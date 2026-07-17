class Solution:

    def findWays(self, matrix, k):
        n = len(matrix)
        m = len(matrix[0])
        mod = 10**9 + 7

        # build suffix sum
        suf = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                suf[i][j] = suf[i + 1][j] + suf[i][j + 1] - suf[i + 1][
                    j + 1] + matrix[i][j]

        # dp[r][c][p] = ways to divide submatrix (r,c)?(n-1,m-1) into p+1 pieces
        dp = [[[0] * k for _ in range(m)] for _ in range(n)]

        # base case: 1 piece, check if submatrix has at least one 1
        for r in range(n):
            for c in range(m):
                dp[r][c][0] = 1 if suf[r][c] > 0 else 0

        for p in range(1, k):

            # suffix sum of dp values over rows for each column
            sufRow = [[0] * m for _ in range(n + 1)]
            for c in range(m):
                for r in range(n - 1, -1, -1):
                    sufRow[r][c] = (sufRow[r + 1][c] + dp[r][c][p - 1]) % mod

            # suffix sum of dp values over cols for each row
            sufCol = [[0] * (m + 1) for _ in range(n)]
            for r in range(n):
                for c in range(m - 1, -1, -1):
                    sufCol[r][c] = (sufCol[r][c + 1] + dp[r][c][p - 1]) % mod

            for r in range(n - 1, -1, -1):
                for c in range(m - 1, -1, -1):
                    if suf[r][c] == 0:
                        continue
                    res = 0

                    # binary search first row where top strip has at least one 1
                    lo, hi = r + 1, n
                    while lo < hi:
                        mid = (lo + hi) // 2
                        if suf[mid][c] < suf[r][c]:
                            hi = mid
                        else:
                            lo = mid + 1
                    if lo < n:
                        res = (res + sufRow[lo][c]) % mod

                    # binary search first col where left strip has at least one 1
                    lo2, hi2 = c + 1, m
                    while lo2 < hi2:
                        mid = (lo2 + hi2) // 2
                        if suf[r][mid] < suf[r][c]:
                            hi2 = mid
                        else:
                            lo2 = mid + 1
                    if lo2 < m:
                        res = (res + sufCol[r][lo2]) % mod

                    dp[r][c][p] = res

        return dp[0][0][k - 1]