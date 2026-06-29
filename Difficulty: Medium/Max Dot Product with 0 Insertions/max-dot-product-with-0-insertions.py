class Solution:

    #Function to find maximum dot product of two arrays.
    def maxDotProduct(self, a, b):
        n = len(a)
        m = len(b)

        # Initializing dp array with -1e9.
        dp = [int(-1e9)] * (m + 1)
        dp[0] = 0

        #iterating over arrays to calculate maximum dot product.
        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + a[i - 1] * b[j - 1])

        return dp[m]