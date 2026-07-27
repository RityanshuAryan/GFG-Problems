class Solution:

    # Recursive function to construct binary tree
    def buildTree(self, pre, preMirror, preIndex, left, right, mp, n):

        # Base case
        if preIndex[0] >= n or left > right:
            return None

        # Create current node
        root = Node(pre[preIndex[0]])
        preIndex[0] += 1

        # If leaf node
        if left == right:
            return root

        # Find next preorder element index
        mirrorIndex = mp[pre[preIndex[0]]]

        # Construct left and right subtree
        if mirrorIndex >= left and mirrorIndex <= right:

            # Construct left subtree
            root.left = self.buildTree(pre, preMirror, preIndex, mirrorIndex,
                                       right, mp, n)

            # Construct right subtree
            root.right = self.buildTree(pre, preMirror, preIndex, left + 1,
                                        mirrorIndex - 1, mp, n)

        return root

    # Function to construct binary tree
    def constructBinaryTree(self, pre, preMirror):

        n = len(pre)

        # Store indices of mirror preorder traversal
        mp = {}

        for i in range(n):
            mp[preMirror[i]] = i

        # Keeps track of current preorder index
        preIndex = [0]

        # Construct and return binary tree
        return self.buildTree(pre, preMirror, preIndex, 0, n - 1, mp, n)