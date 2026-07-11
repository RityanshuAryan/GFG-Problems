class Solution:

    def dfs(self, mat, vis, i, j, xd, yd):
        n = len(mat)
        m = len(mat[0])

        # Return -1 if cell is out of bounds,
        # blocked, or already visited
        if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] == 0 or vis[i][j]:
            return -1

        # Destination reached
        if i == xd and j == yd:
            return 0

        # Mark current cell as visited
        vis[i][j] = True

        # Store longest path length from current cell
        ans = -1

        # Possible moves: right, left, down, up
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        # Explore all four directions
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            curr = self.dfs(mat, vis, ni, nj, xd, yd)

            # Update answer if destination is reachable
            if curr != -1:
                ans = max(ans, curr + 1)

        # Backtrack so this cell can be used
        # in other possible paths
        vis[i][j] = False

        return ans

    def longestPath(self, mat, xs, ys, xd, yd):

        # If source or destination is blocked
        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1

        n = len(mat)
        m = len(mat[0])

        # Visited matrix to avoid revisiting cells
        vis = [[False] * m for _ in range(n)]

        return self.dfs(mat, vis, xs, ys, xd, yd)