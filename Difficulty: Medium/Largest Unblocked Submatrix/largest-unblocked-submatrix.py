class Solution:

    def largestArea(self, n, m, arr):

        r = []
        c = []

        for it in arr:
            r.append(it[0])
            c.append(it[1])

        # Add boundaries
        r.append(0)
        r.append(n + 1)

        c.append(0)
        c.append(m + 1)

        r.sort()
        c.sort()

        maxr = 0
        maxc = 0

        # Find maximum gap in rows
        for i in range(1, len(r)):
            maxr = max(maxr, r[i] - r[i - 1] - 1)

        # Find maximum gap in columns
        for i in range(1, len(c)):
            maxc = max(maxc, c[i] - c[i - 1] - 1)

        return maxr * maxc