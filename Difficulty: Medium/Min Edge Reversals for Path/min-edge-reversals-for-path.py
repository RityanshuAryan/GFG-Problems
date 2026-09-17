class Solution:

    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int,
                            dst: int) -> int:
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:

            # Original edge has zero reversal cost.
            adj[u].append((v, 0))

            # Reversed edge costs one reversal.
            adj[v].append((u, 1))

        dist = [float('inf')] * (n + 1)
        dq = deque()

        dist[src] = 0
        dq.appendleft(src)

        while dq:
            node = dq.popleft()

            for nxt, wt in adj[node]:
                if dist[node] + wt < dist[nxt]:
                    dist[nxt] = dist[node] + wt

                    # Prioritize zero-cost edges in 0-1 BFS.
                    if wt == 0:
                        dq.appendleft(nxt)
                    else:
                        dq.append(nxt)

        return -1 if dist[dst] == float('inf') else dist[dst]