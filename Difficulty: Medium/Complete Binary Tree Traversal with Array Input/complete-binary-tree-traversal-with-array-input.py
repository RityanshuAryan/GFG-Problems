class Solution:

    def levelSort(self, arr):
        res = []
        n = len(arr)

        # 'start' marks the beginning index of the current level.
        start = 0

        # 'level' is used to determine the number of nodes
        # that can be present at each level.
        level = 1

        while start < n:
            # Compute the ending index (exclusive) of the current level.
            end = min((1 << level) - 1, n)

            # Sort only the elements belonging to the current level.
            arr[start:end] = sorted(arr[start:end])

            # Store the sorted values of the current level.
            curr = []
            for i in range(start, end):
                curr.append(arr[i])

            res.append(curr)

            # Move to the next level.
            start = end
            level += 1

        return res