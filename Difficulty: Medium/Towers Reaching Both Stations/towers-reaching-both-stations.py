class Solution:

    # Direction vectors for moving right, left, down and up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Check whether a cell lies inside the grid
    def isValid(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m

    # BFS to find towers reachable from a control station
    def bfs(self, strength, n, m, queue, reachable):
        while queue:
            row, col = queue.popleft()

            # Visit all neighbouring towers
            for dx, dy in self.directions:
                newRow, newCol = row + dx, col + dy

                # Signal can propagate only to towers having
                # strength greater than or equal to the current tower
                if (self.isValid(newRow, newCol, n, m)
                        and not reachable[newRow][newCol]
                        and strength[newRow][newCol] >= strength[row][col]):

                    reachable[newRow][newCol] = True
                    queue.append((newRow, newCol))

    def countCoordinates(self, mat):
        if not mat:
            return 0

        n = len(mat)
        m = len(mat[0])

        stationP = deque()
        stationQ = deque()

        # Stores towers reachable from Station P and Station Q
        reachP = [[False] * m for _ in range(n)]
        reachQ = [[False] * m for _ in range(n)]

        # Towers adjacent to Station P (top boundary)
        # and Station Q (bottom boundary)
        for j in range(m):
            stationP.append((0, j))
            reachP[0][j] = True

            stationQ.append((n - 1, j))
            reachQ[n - 1][j] = True

        # Towers adjacent to Station P (left boundary)
        # and Station Q (right boundary)
        for i in range(n):
            stationP.append((i, 0))
            reachP[i][0] = True

            stationQ.append((i, m - 1))
            reachQ[i][m - 1] = True

        # Run BFS from both stations
        self.bfs(mat, n, m, stationP, reachP)
        self.bfs(mat, n, m, stationQ, reachQ)

        count = 0

        # Count towers reachable from both stations
        for i in range(n):
            for j in range(m):
                if reachP[i][j] and reachQ[i][j]:
                    count += 1

        return count