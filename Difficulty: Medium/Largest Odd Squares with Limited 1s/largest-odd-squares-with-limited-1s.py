class Solution:

    def largestSquare(self, mat: list[list[int]], queries: list[list[int]],
                      k: int) -> list[int]:
        n, m = len(mat), len(mat[0])

        # Build a 1-indexed 2D prefix sum for O(1) rectangle sum queries
        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                prefix[i + 1][j + 1] = (prefix[i][j + 1] + prefix[i + 1][j] -
                                        prefix[i][j] + mat[i][j])

        res = []

        for i, j in queries:
            min_dist = min(i, j, n - i - 1, m - j - 1)

            # Even the single center cell exceeds k -- no valid square at all
            if mat[i][j] > k:
                res.append(-1)
                continue

            # Binary search for the largest radius rad whose square sum stays within k
            lo, hi, best = 0, min_dist, 0

            while lo <= hi:
                mid = (lo + hi) // 2
                r1, c1 = i - mid, j - mid
                r2, c2 = i + mid, j + mid

                s = (prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] -
                     prefix[r2 + 1][c1] + prefix[r1][c1])

                if s <= k:
                    best = mid
                    lo = mid + 1
                else:
                    hi = mid - 1

            res.append(2 * best + 1)

        return res