class Solution:

    def countWays(self, s1, s2):
        n = len(s1)
        m = len(s2)

        # Create a table to store results of sub-problems
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(m + 1):
            dp[0][i] = 0
        for i in range(n + 1):
            dp[i][0] = 1

        mod = 10**9 + 7

        # Fill the table in a bottom-up manner
        for i in range(1, n + 1):
            for j in range(1, m + 1):

                # If last characters are the same, we have two options:
                # 1. Consider last characters of both strings in the solution
                # 2. Ignore the last character of the first string
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod
                else:

                    # If last characters are different, ignore the last character of the first string
                    dp[i][j] = dp[i - 1][j] % mod

        return dp[n][m] % mod