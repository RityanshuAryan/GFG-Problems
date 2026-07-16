class Solution:
    # Function to count n-digit numbers
    # with sum of digits as the target.
    def countWays(self, n, sum):
        if sum > 9 * n:
            return -1

        # dp[len][s] = count of len-digit sequences
        # having digit sum equal to s.
        dp = [[0] * (sum + 1) for _ in range(n + 1)]

        dp[0][0] = 1

        # Build the DP table.
        for length in range(1, n + 1):
            for s in range(sum + 1):
                for digit in range(10):
                    if s >= digit:
                        dp[length][s] += dp[length - 1][s - digit]

        ans = 0

        # First digit must be from 1 to 9.
        for digit in range(1, 10):
            if sum >= digit:
                ans += dp[n - 1][sum - digit]

        return -1 if ans == 0 else ans