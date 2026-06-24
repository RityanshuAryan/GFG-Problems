class Solution:

    # Function to recursively find the shortest path
    def solve(self, i, j, mat, ans, dp):

        n = len(mat)

        # Check if out of bounds
        if i >= n or j >= n:
            return False

        # Check if destination reached
        if i == n - 1 and j == n - 1:
            ans[i][j] = 1
            return True

        if mat[i][j] == 0:
            return False

        # Check if already visited
        if dp[i][j] != -1:
            return dp[i][j] == 1

        ans[i][j] = 1

        jump = mat[i][j]

        # Try shortest jumps first
        for step in range(1, jump + 1):

            # Try moving right first
            if self.solve(i, j + step, mat, ans, dp):
                dp[i][j] = 1
                return True

            # Try moving down
            if self.solve(i + step, j, mat, ans, dp):
                dp[i][j] = 1
                return True

        ans[i][j] = 0

        dp[i][j] = 0
        return False

    # Main function to find the shortest path in the matrix
    def shortestDist(self, mat):

        n = len(mat)

        # Special case for matrix of size 1
        if n == 1:
            return [[1]]

        ans = [[0 for _ in range(n)] for _ in range(n)]

        if mat[0][0] == 0:
            return [[-1]]

        dp = [[-1 for _ in range(n)] for _ in range(n)]

        # Call recursive function to find shortest path
        if not self.solve(0, 0, mat, ans, dp):
            return [[-1]]

        return ans