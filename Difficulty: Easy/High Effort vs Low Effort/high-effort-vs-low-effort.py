class Solution:

    def maxTask(self, h: list[int], l: list[int]) -> int:
        n = len(h)

        # edge case: no days
        if n == 0:
            return 0

        # prev2 -> dp[i-2], prev1 -> dp[i-1]
        prev2 = 0

        # day 0: choose best of h or l
        prev1 = max(h[0], l[0])

        # if only one day
        if n == 1:
            return prev1

        # day 1: either take h, or l + prev best
        curr = max(h[1], l[1] + prev1)

        prev2 = prev1
        prev1 = curr

        # process remaining days
        for i in range(2, n):
            # option 1: take l today + best till yesterday
            # option 2: take h today + best till day before yesterday
            curr = max(l[i] + prev1, h[i] + prev2)

            prev2 = prev1
            prev1 = curr

        return prev1