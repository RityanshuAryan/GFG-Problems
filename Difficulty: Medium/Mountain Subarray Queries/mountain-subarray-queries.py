class Solution:

    def processQueries(self, arr, queries):
        n = len(arr)

        # dec[i] stores the farthest index reachable
        # from i while maintaining a non-decreasing sequence.
        dec = [0] * n
        dec[n - 1] = n - 1

        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                dec[i] = dec[i + 1]
            else:
                dec[i] = i

        # inc[i] stores the farthest index reachable
        # from i while maintaining a non-increasing sequence.
        inc = [0] * n
        inc[0] = 0

        for i in range(1, n):
            if arr[i] <= arr[i - 1]:
                inc[i] = inc[i - 1]
            else:
                inc[i] = i

        ans = []

        for l, r in queries:
            ans.append(dec[l] >= inc[r])

        return ans