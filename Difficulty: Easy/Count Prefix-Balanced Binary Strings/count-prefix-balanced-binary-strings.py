class Solution:
    
    def prefixStrings(self, n: int) -> int:
        mod = 1000000007

        dp = [0] * (n + 1)

        # Base case for Catalan numbers.
        dp[0] = 1

        if n >= 1:
            dp[1] = 1

        # Compute Catalan numbers using dynamic programming.
        for i in range(2, n + 1):

            res = 0

            for j in range(i):
                res = (res + dp[j] * dp[i - j - 1]) % mod

            dp[i] = res

        return dp[n]