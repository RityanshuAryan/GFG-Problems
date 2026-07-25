class Solution:

    def maximumSum(self, mat, k):
        n = len(mat)

        # 1D column sum array — O(n) space
        colSum = [0] * n
        res = float('-inf')

        for i in range(n):

            # Update column sums with new row entering and old row leaving window
            for j in range(n):
                colSum[j] += mat[i][j]
                if i >= k:
                    colSum[j] -= mat[i - k][j]

            # Slide horizontal window of size k over colSum
            if i >= k - 1:
                windowSum = 0
                for j in range(n):
                    windowSum += colSum[j]
                    if j >= k:
                        windowSum -= colSum[j - k]
                    if j >= k - 1:
                        res = max(res, windowSum)

        return res