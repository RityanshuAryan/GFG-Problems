class Solution:

    # Performs inorder traversal and updates the minimum difference.
    def inorder(self, root, prev, minDiff):

        if root is None:
            return

        self.inorder(root.left, prev, minDiff)

        # Update the minimum difference with the previous node.
        if prev[0] != -1:
            minDiff[0] = min(minDiff[0], root.data - prev[0])

        prev[0] = root.data

        self.inorder(root.right, prev, minDiff)

    def absDiff(self, root):

        prev = [-1]
        minDiff = [float('inf')]

        self.inorder(root, prev, minDiff)

        return minDiff[0]