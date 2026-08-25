class Solution:

    def minMoves(self, arr):
        n = len(arr)
        dp = [0] * (n + 1)

        # Compute the longest consecutive increasing subsequence.
        for x in arr:
            dp[x] = dp[x - 1] + 1

        longest = 0

        # Find the maximum subsequence length.
        for i in range(1, n + 1):
            longest = max(longest, dp[i])

        return n - longest