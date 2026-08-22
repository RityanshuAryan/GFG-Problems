''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''


class Solution:

    # Finds LCA of two given nodes
    def findLCA(self, root, p, q):

        if root is None:
            return None

        if root.data == p or root.data == q:
            return root

        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)

        if left and right:
            return root

        return left if left else right

    # Stores path from root to target node using L/R directions
    def findPath(self, root, target, path):

        if root is None:
            return False

        if root.data == target:
            return True

        # Try going left
        path.append('L')

        if self.findPath(root.left, target, path):
            return True

        path.pop()

        # Try going right
        path.append('R')

        if self.findPath(root.right, target, path):
            return True

        path.pop()

        return False

    # Counts direction changes in a path
    def countTurns(self, path):

        turns = 0

        for i in range(1, len(path)):

            if path[i] != path[i - 1]:
                turns += 1

        return turns

    # Returns number of turns required from first node to second node
    def numberOfTurns(self, root, p, q):

        lca = self.findLCA(root, p, q)

        if lca is None:
            return -1

        pathFirst = []
        pathSecond = []

        # Paths from LCA to both nodes
        self.findPath(lca, p, pathFirst)
        self.findPath(lca, q, pathSecond)

        if lca.data == p or lca.data == q:

            path = pathSecond if lca.data == p else pathFirst

            turns = self.countTurns(path)

        else:

            # Add one turn for changing direction at LCA
            turns = (self.countTurns(pathFirst) + self.countTurns(pathSecond) +
                     1)

        # No turns means straight path
        return -1 if turns == 0 else turns