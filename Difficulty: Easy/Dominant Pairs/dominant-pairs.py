class Solution:

    def dominantPairs(self, arr: list[int]) -> int:

        n = len(arr)
        mid = n // 2

        # Sort both halves independently.
        arr[:mid] = sorted(arr[:mid])
        arr[mid:] = sorted(arr[mid:])

        res = 0
        right = mid

        # Count dominant pairs using two pointers.
        for left in range(mid):

            while right < n and arr[left] >= 5 * arr[right]:
                right += 1

            res += right - mid

        return res