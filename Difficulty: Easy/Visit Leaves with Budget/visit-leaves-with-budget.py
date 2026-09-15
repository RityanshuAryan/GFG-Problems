''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
        def getCount(self, root, k):
            if root is None:
                return 0

            q = deque()
            q.append(root)

            level = 1
            cnt = 0

            # Perform level order traversal
            while q:
                size = len(q)
                leafCount = 0

                # Process all nodes at current level
                for i in range(size):
                    curr = q.popleft()

                    # Count leaf nodes
                    if curr.left is None and curr.right is None:
                        leafCount += 1

                    # Add children for next level
                    if curr.left is not None:
                        q.append(curr.left)

                    if curr.right is not None:
                        q.append(curr.right)

                # Find how many leaves can be visited
                canVisit = k // level
                take = min(leafCount, canVisit)

                # Update answer and remaining budget
                cnt += take
                k -= take * level

                # No leaf at this or later level can be visited
                if k < level:
                    break

                level += 1

            return cnt