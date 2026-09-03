class Solution:

    def maxDiffSum(self, arr):
        n = len(arr)

        # dp[i][0] stores the maximum sum when the i-th element is changed to 1
        # dp[i][1] stores the maximum sum when the i-th element remains unchanged
        dp = [[0] * 2 for _ in range(n)]

        # Fill the DP table
        for i in range(n - 1):

            # Case 1: Current element is changed to 1
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + abs(1 - arr[i]))

            # Case 2: Current element remains as arr[i + 1]
            dp[i + 1][1] = max(dp[i][0] + abs(arr[i + 1] - 1),
                               dp[i][1] + abs(arr[i + 1] - arr[i]))

        # Return the maximum possible difference sum
        return max(dp[n - 1][0], dp[n - 1][1])