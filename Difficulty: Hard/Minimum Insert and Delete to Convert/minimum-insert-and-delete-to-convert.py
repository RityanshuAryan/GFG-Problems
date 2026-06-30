class Solution:

    def minInsAndDel(self, a, b):
        n = len(a)
        m = len(b)

        # Store index of elements in b
        mp = {}

        for i in range(m):
            mp[b[i]] = i

        # Store mapped indices
        v = []

        # Traverse array a
        for x in a:
            # If element is present in b
            if x in mp:
                v.append(mp[x])

        # Stores LIS
        lis = []

        # Find LIS of mapped indices
        for x in v:
            # Find position using lower_bound
            it = self.lower_bound(lis, x)

            # Insert element
            if it == len(lis):
                lis.append(x)
            # Replace element
            else:
                lis[it] = x

        # Length of LCS
        len_lis = len(lis)

        # Store final answer
        res = (n - len_lis) + (m - len_lis)

        return res

    def lower_bound(self, lis, x):
        lo, hi = 0, len(lis)
        while lo < hi:
            mid = (lo + hi) // 2
            if lis[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo