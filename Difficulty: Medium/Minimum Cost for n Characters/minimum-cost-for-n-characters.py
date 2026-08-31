class Solution:

    def minCost(self, n: int, i: int, d: int, c: int) -> int:

        # No characters are required.
        if n == 0:
            return 0

        # One insert is needed to obtain a single character.
        if n == 1:
            return i

        # dp[x] stores the minimum cost to obtain exactly x characters.
        dp = [0] * (n + 1)

        dp[1] = i

        # Compute the minimum cost for every length from 2 to n.
        for x in range(2, n + 1):
            if x % 2 == 0:

                # Even length:
                # 1) Insert one character after reaching x - 1.
                # 2) Copy-paste from x / 2 characters.
                dp[x] = min(dp[x - 1] + i, dp[x // 2] + c)

            else:

                # Odd length:
                # 1) Insert one character after reaching x - 1.
                # 2) Copy-paste from (x + 1) / 2 characters,
                #    then delete the extra character.
                dp[x] = min(dp[x - 1] + i, dp[(x + 1) // 2] + c + d)

        return dp[n]