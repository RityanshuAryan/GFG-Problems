class Solution:
    # Returns the longest distance from src to every vertex.
    def maxDistance(self, V, src, edges):

        # Build the adjacency list and indegree array.
        g = [[] for _ in range(V)]
        indegree = [0] * V

        for u, v, wt in edges:
            g[u].append((v, wt))
            indegree[v] += 1

        # Kahn's Algorithm to obtain a topological ordering.
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topoOrder = []

        while q:
            node = q.popleft()
            topoOrder.append(node)

            for nxt, wt in g[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        # Initialize all distances as unreachable.
        INT_MIN = -(2**31)
        dist = [INT_MIN] * V
        dist[src] = 0

        # Process vertices in topological order and
        # relax outgoing edges to compute longest paths.
        for node in topoOrder:

            # Skip unreachable vertices.
            if dist[node] == INT_MIN:
                continue

            for nxt, wt in g[node]:
                dist[nxt] = max(dist[nxt], dist[node] + wt)

        return dist