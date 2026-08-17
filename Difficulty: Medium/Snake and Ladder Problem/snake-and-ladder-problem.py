class Solution:
    def minThrows(self, n, lad, sn):
        cells = n * n
        moves = [-1] * (cells + 1)
        vis = [False] * (cells + 1)

        # Store ladders safely
        for i in range(0, len(lad) - 1, 2):
            moves[lad[i]] = lad[i + 1]

        # Store snakes safely
        for i in range(0, len(sn) - 1, 2):
            moves[sn[i]] = sn[i + 1]

        # BFS: (current cell, number of dice throws)
        q = deque()
        q.append((1, 0))
        vis[1] = True

        while q:
            pos, dist = q.popleft()

            if pos == cells:
                return dist

            # Try all possible dice outcomes
            for nxt in range(pos + 1, min(pos + 6, cells) + 1):
                if not vis[nxt]:
                    vis[nxt] = True
                    dest = nxt if moves[nxt] == -1 else moves[nxt]
                    q.append((dest, dist + 1))

        return -1