class Solution:

    def isPossible(self, arr, s, x):

        # Generate the sequence written on the paper.
        pref = [0] * (len(arr) + 1)

        pref[0] = s
        prefSum = s

        for i in range(len(arr)):
            pref[i + 1] = prefSum + arr[i]
            prefSum += pref[i + 1]

        # Greedily subtract the largest possible values.
        target = x

        for i in range(len(pref) - 1, -1, -1):
            if pref[i] <= target:
                target -= pref[i]

        # Check if the required sum is formed.
        return target == 0