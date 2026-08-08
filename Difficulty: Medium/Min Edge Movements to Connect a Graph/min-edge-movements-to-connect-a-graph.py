class Solution:
    # Find the representative (root) of a set
    # Path compression flattens the tree, making future finds faster
    def find(self, x, parent):
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)
        return parent[x]

    def minEdgesReq(self, n, edges):

        # At least (n - 1) edges are needed to connect n nodes
        if len(edges) < n - 1:
            return -1

        # Initially every node is its own parent
        parent = list(range(n))

        # Size of each component
        size = [1] * n

        for u, v in edges:

            ru = self.find(u, parent)
            rv = self.find(v, parent)

            # Already in the same component
            if ru == rv:
                continue

            # Attach the smaller component to the larger one
            if size[ru] < size[rv]:
                ru, rv = rv, ru

            parent[rv] = ru
            size[ru] += size[rv]

        components = 0

        # Count the number of connected components
        for i in range(n):
            if self.find(i, parent) == i:
                components += 1

        # Need (components - 1) edges to connect all components
        return components - 1