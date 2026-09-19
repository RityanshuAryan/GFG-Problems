class Solution:

    # Returns the length of the Longest Common Subsequence.
    def lcs(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        prev = [0] * (m + 1)
        curr = [0] * (m + 1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                # If characters match, include this character in LCS.
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + 1

                # Otherwise, skip one character from either string.
                else:
                    curr[j] = max(prev[j], curr[j - 1])

            # Move current row to previous row.
            prev = curr
            curr = [0] * (m + 1)

        return prev[m]

    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:

        n = len(s1)
        m = len(s2)

        # Keep s2 as the shorter string to reduce space.
        if m > n:
            s1, s2 = s2, s1
            costS1, costS2 = costS2, costS1
            n, m = m, n

        # Find the maximum number of characters
        # that can be kept common in both strings.
        lcsLength = self.lcs(s1, s2)

        # Characters not part of the LCS must be deleted.
        deleteFromS1 = n - lcsLength
        deleteFromS2 = m - lcsLength

        return deleteFromS1 * costS1 + deleteFromS2 * costS2