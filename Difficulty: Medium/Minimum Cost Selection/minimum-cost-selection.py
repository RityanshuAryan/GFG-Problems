class Solution:

    def minCost(self, mat):
        n = len(mat)

        prev0 = mat[0][0]
        prev1 = mat[0][1]
        prev2 = mat[0][2]

        for i in range(1, n):
            # Cost if current row selects first choice.
            curr0 = mat[i][0] + min(prev1, prev2)

            # Cost if current row selects second choice.
            curr1 = mat[i][1] + min(prev0, prev2)

            # Cost if current row selects third choice.
            curr2 = mat[i][2] + min(prev0, prev1)

            prev0 = curr0
            prev1 = curr1
            prev2 = curr2

        return min(prev0, prev1, prev2)