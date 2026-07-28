class Solution:

    def shortestPath(self, V: int, src: int, dest: int,
                     edges: list[list[int]]) -> int:
        extra = V

        # Create adjacency list. Extra nodes
        # are used to split weight 2 edges.
        adj = [[] for _ in range(V + len(edges))]

        for e in edges:
            u = e[0]
            v = e[1]
            wt = e[2]

            if wt == 1:
                # Weight 1 edge remains unchanged.
                adj[u].append(v)
                adj[v].append(u)
            else:
                # Convert weight 2 edge into two weight 1 edges:
                # u -- 1 -- newNode -- 1 -- v
                adj[u].append(extra)
                adj[extra].append(v)

                adj[v].append(extra)
                adj[extra].append(u)

                extra += 1

        # BFS on the transformed unweighted
        # graph gives shortest distance.
        dist = [-1] * extra
        from collections import deque
        q = deque()
        q.append(src)
        dist[src] = 0

        while q:
            node = q.popleft()

            if node == dest:
                return dist[node]

            for nxt in adj[node]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[node] + 1
                    q.append(nxt)

        # Destination is not reachable from source.
        return -1