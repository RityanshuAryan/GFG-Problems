class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        n = len(arr)
        total = 0

        for i in range(m):
            total += arr[i]

        res = total
        left = 0

        for right in range(m, n + m):
            total -= arr[left]
            total += arr[right % n]

            res = max(res, total)
            left += 1

        return res