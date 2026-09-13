class Solution:

    def bfs(self, adj, start):
        n = len(adj)

        dist = [-1] * n
        q = deque()

        dist[start] = 0
        q.append(start)

        farthestNode = start
        farthestDist = 0

        while q:
            node = q.popleft()

            for nextNode in adj[node]:
                nextNode -= 1

                if dist[nextNode] == -1:
                    dist[nextNode] = dist[node] + 1
                    q.append(nextNode)

                    if dist[nextNode] > farthestDist:
                        farthestDist = dist[nextNode]
                        farthestNode = nextNode

        return farthestNode, farthestDist

    def partyHouse(self, adj: list[list[int]]) -> int:
        first = self.bfs(adj, 0)
        diameterEnd = first[0]

        second = self.bfs(adj, diameterEnd)
        diameter = second[1]

        return (diameter + 1) // 2