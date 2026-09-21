class Solution:

    def areAnagrams(self, root1, root2):
        # If both trees are empty, they are anagrams.
        # If only one is empty, they cannot be anagrams.
        if root1 is None or root2 is None:
            return root1 is root2

        # Use separate queues to traverse both trees level by level.
        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            # Get the number of nodes at the current level.
            n1 = len(q1)
            n2 = len(q2)

            # Corresponding levels must contain the same number of nodes.
            if n1 != n2:
                return False

            # Store the frequency difference between the two levels.
            freq = {}

            # Process the current level of both trees.
            for _ in range(n1):
                node1 = q1.popleft()
                node2 = q2.popleft()

                # Increase frequency for values from the first tree
                # and decrease it for values from the second tree.
                freq[node1.data] = freq.get(node1.data, 0) + 1
                freq[node2.data] = freq.get(node2.data, 0) - 1

                # Add children for processing the next level.
                if node1.left is not None:
                    q1.append(node1.left)

                if node1.right is not None:
                    q1.append(node1.right)

                if node2.left is not None:
                    q2.append(node2.left)

                if node2.right is not None:
                    q2.append(node2.right)

            # Every frequency must be zero if the levels are anagrams.
            for value in freq.values():
                if value != 0:
                    return False

        # All corresponding levels matched.
        return not q1 and not q2