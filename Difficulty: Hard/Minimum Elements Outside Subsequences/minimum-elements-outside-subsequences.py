class Solution:

        def solve(self, idx, incLast, decLast, arr, dp):
            if idx == len(arr):
                return 0

            if dp[idx][incLast + 1][decLast + 1] != -1:
                return dp[idx][incLast + 1][decLast + 1]

            # Skip the current element.
            res = 1 + self.solve(idx + 1, incLast, decLast, arr, dp)

            # Include the current element in the increasing subsequence.
            if incLast == -1 or arr[idx] > arr[incLast]:
                res = min(res, self.solve(idx + 1, idx, decLast, arr, dp))

            # Include the current element in the decreasing subsequence.
            if decLast == -1 or arr[idx] < arr[decLast]:
                res = min(res, self.solve(idx + 1, incLast, idx, arr, dp))

            dp[idx][incLast + 1][decLast + 1] = res
            return res

        def minCount(self, arr):
            n = len(arr)

            # Memoize the minimum skipped elements for every DP state.
            dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(n)]

            # Start with both subsequences empty.
            return self.solve(0, -1, -1, arr, dp)