class Solution:

    def canRepresentBST(self, arr):
        # Create an empty stack
        s = []

        # Initialize current root as minimum possible value
        root = float('-inf')

        # Traverse given array
        for i in range(len(arr)):
            # If we find a node who is on right side and smaller than root, return false
            if arr[i] < root:
                return False

            # If arr[i] is in right subtree of stack top,
            # Keep removing items smaller than arr[i] and make the last removed item as new root.
            while s and s[-1] < arr[i]:
                root = s.pop()

            # At this point either stack is empty or arr[i] is smaller than root, push arr[i]
            s.append(arr[i])
        return True