class Solution:

    def countStrings(self, n, k):

        #initialize dynamic programming array with size (n+1)x(k+1)x2
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]

        #base cases where n=1
        dp[1][0][0] = 1
        dp[1][0][1] = 1

        #filling up the dp array using recurrence relation
        for i in range(2, n + 1):
            for j in range(k + 1):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % (10**9 + 7)
                dp[i][j][1] = dp[i - 1][j][0]
                if j >= 1:
                    dp[i][j][1] += dp[i - 1][j - 1][1]

        #returning the final count of strings
        return (dp[n][k][0] + dp[n][k][1]) % (10**9 + 7)