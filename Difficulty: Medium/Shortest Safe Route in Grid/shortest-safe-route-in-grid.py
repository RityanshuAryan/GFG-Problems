class Solution:

        # Changes in row to move up, stay, stay, move down
        rowNum = [-1, 0, 0, 1]

        # Changes in column to move left, stay, move right, stay
        colNum = [0, -1, 1, 0]

        # n and m are completely removed from the arguments
        def shortestPath(self, mat: list[list[int]]) -> int:
            n = len(mat)
            if n == 0:
                return -1
            m = len(mat[0])
            if m == 0:
                return -1

            # Queue to perform BFS {x, y, distance}
            q = []

            # C++ Standard way to initialize a 2D dynamic array/matrix (replaces VLA)
            d = [[1e9] * m for _ in range(n)]

            # Lambda function to check if cell is within bounds
            def isValid(i, j):
                return (i >= 0 and i < n and j >= 0 and j < m)

            # Lambda function to check if cell and its adjacent cells are safe
            def check(i, j):
                if not isValid(i, j):
                    return False

                # Must check if the current cell itself is a landmine!
                if mat[i][j] == 0:
                    return False

                for k in range(4):
                    nx = i + self.rowNum[k]
                    ny = j + self.colNum[k]
                    if isValid(nx, ny) and mat[nx][ny] == 0:
                        return False
                return True

            # Pushing safe cells from the rightmost column into the queue
            for i in range(n):
                if check(i, m - 1):
                    q.append((i, m - 1, 1))

                    # Mark distance immediately to avoid duplicate processing
                    d[i][m - 1] = 1

            # BFS traversal
            while q:
                z = q.pop(0)
                x, y, dis = z

                # Check 4 directional neighbors
                for k in range(4):
                    nx = x + self.rowNum[k]
                    ny = y + self.colNum[k]

                    # If neighbor is safe and offers a shorter path
                    if check(nx, ny) and d[nx][ny] > dis + 1:
                        d[nx][ny] = dis + 1  # Update distance BEFORE pushing
                        q.append((nx, ny, dis + 1))

            # Finding the minimum distance in the first column
            ans = 1e9
            for i in range(n):
                ans = min(ans, d[i][0])

            # If no safe path found, return -1
            return -1 if ans >= 1e9 else ans