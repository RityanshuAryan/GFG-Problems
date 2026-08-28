class Solution:
    
    def countSubsequences(self, s, n):
        mod = 1000000007

        # dp[rem] stores the number of subsequences having remainder rem modulo n.
        dp = [0] * n

        for ch in s:
            digit = ord(ch) - ord('0')
            curr = dp[:]

            # Start a new subsequence with the current digit.
            curr[digit % n] = (curr[digit % n] + 1) % mod
            for rem in range(n):

                # Append the current digit to all existing subsequences.
                nextRem = (rem * 10 + digit) % n
                curr[nextRem] = (curr[nextRem] + dp[rem]) % mod

            # Move to the next digit.
            dp = curr
        return dp[0]