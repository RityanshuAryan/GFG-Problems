class Solution:

    def minDeletions(self, arr):

        # tails stores smallest tail element of LIS of each length
        tails = []

        for num in arr:

            # Find position to replace using binary search
            pos = bisect.bisect_left(tails, num)

            # Extend LIS if num is greater than all tails
            if pos == len(tails):
                tails.append(num)

            # Replace to maintain smallest possible tail
            else:
                tails[pos] = num

        # Min deletions = n - LIS length
        return len(arr) - len(tails)