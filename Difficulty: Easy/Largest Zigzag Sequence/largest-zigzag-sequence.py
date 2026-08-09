class Solution:

    def zigzagSequence(self, mat):
        n = len(mat)

        # DP values for the previous row
        prev = mat[0][:]

        for i in range(1, n):
            max1 = max2 = -1
            max_col = -1

            # Find the maximum and second maximum values from the previous row
            for j in range(n):
                if prev[j] > max1:
                    max2 = max1
                    max1 = prev[j]
                    max_col = j
                elif prev[j] > max2:
                    max2 = prev[j]

            curr = [0] * n

            for j in range(n):

                # Use second maximum if the current column is the same as the column of the maximum value
                curr[j] = mat[i][j] + (max2 if j == max_col else max1)

            # Move to the next row
            prev = curr

        # Find the maximum zigzag sum
        return max(prev)