class Solution:

    def countSub(self, arr, x):
        n = len(arr)

        st = 0
        end = 0

        sum = 0
        cnt = 0

        while end < n:
            sum += arr[end]

            while st <= end and sum > x:
                sum -= arr[st]
                st += 1

            cnt += (end - st + 1)

            end += 1

        return cnt

    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        rcnt = self.countSub(arr, r)
        lcnt = self.countSub(arr, l - 1)

        return rcnt - lcnt   