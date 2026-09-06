class Solution:

        def pairAndSum(self, arr):
            ans = 0

            # Traverse over all bits
            for i in range(32):

                # Count number of elements with i'th bit set
                k = 0
                for j in range(len(arr)):
                    if arr[j] & (1 << i):
                        k += 1

                ans += (1 << i) * (k * (k - 1) // 2)

            return ans