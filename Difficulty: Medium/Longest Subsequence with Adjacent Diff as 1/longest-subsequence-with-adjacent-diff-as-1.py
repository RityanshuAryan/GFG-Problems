class Solution:

        def longestSubseq(self, arr):
            MAX = 1000000
            dp = [0] * (MAX + 2)

            ans = 0

            for x in arr:
                # Extend the best subsequence ending with a neighboring value
                dp[x] = max(dp[x], max(dp[x - 1], dp[x + 1]) + 1)

                # Track the maximum subsequence length found so far
                ans = max(ans, dp[x])

            return ans