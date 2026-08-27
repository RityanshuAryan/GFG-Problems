class Solution:

    def maxArea(self, mat: list[list[int]]) -> int:
        r = len(mat)
        c = len(mat[0])

        # Compute heights of consecutive 1s
        for i in range(1, r):
            for j in range(c):
                if mat[i][j]:
                    mat[i][j] += mat[i - 1][j]

        ans = 0

        # Process each row
        for i in range(r):
            arr = mat[i][:]

            # Bring taller columns together
            arr.sort(reverse=True)

            # Find the maximum area for this row
            for j in range(c):
                ans = max(ans, arr[j] * (j + 1))

        return ans