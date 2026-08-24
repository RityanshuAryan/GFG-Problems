class Solution:

    def isValid(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m

    def numberOfCells(self, r: int, c: int, u: int, d: int,
                      mat: list[list[int]]) -> int:
        n = len(mat)

        if n == 0:
            return 0

        m = len(mat[0])

        if r < 0 or r >= n or c < 0 or c >= m:
            return 0

        # If the starting cell is blocked, Geek cannot move.
        if mat[r][c] == '#':
            return 0

        pq = []

        vis = [[False] * m for _ in range(n)]

        # Store (upMoves, downMoves, row, col).
        heapq.heappush(pq, (0, 0, r, c))
        vis[r][c] = True

        while pq:

            up, down, x, y = heapq.heappop(pq)

            # Move to the upper cell if the move limit allows.
            if (self.isValid(x - 1, y, n, m) and not vis[x - 1][y]
                    and mat[x - 1][y] == '.' and up + 1 <= u):

                vis[x - 1][y] = True
                heapq.heappush(pq, (up + 1, down, x - 1, y))

            # Move to the lower cell if the move limit allows.
            if (self.isValid(x + 1, y, n, m) and not vis[x + 1][y]
                    and mat[x + 1][y] == '.' and down + 1 <= d):

                vis[x + 1][y] = True
                heapq.heappush(pq, (up, down + 1, x + 1, y))

            # Move to the left cell without affecting move limits.
            if (self.isValid(x, y - 1, n, m) and not vis[x][y - 1]
                    and mat[x][y - 1] == '.'):

                vis[x][y - 1] = True
                heapq.heappush(pq, (up, down, x, y - 1))

            # Move to the right cell without affecting move limits.
            if (self.isValid(x, y + 1, n, m) and not vis[x][y + 1]
                    and mat[x][y + 1] == '.'):

                vis[x][y + 1] = True
                heapq.heappush(pq, (up, down, x, y + 1))

        res = 0

        # Count all reachable cells.
        for i in range(n):
            for j in range(m):
                res += vis[i][j]

        return res