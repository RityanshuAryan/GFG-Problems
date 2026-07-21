class Solution:

    def maxIndexDifference(self, s):
        n = len(s)

        # best[i] stores the farthest reachable
        # index for character ('a' + i)
        best = [-1] * 26

        # Remains -1 if no valid starting index ('a') exists
        ans = -1

        # Process from right to left to
        # consider only jumps to the right
        for i in range(n - 1, -1, -1):
            farthest = i

            # Jump to the next alphabet
            # character if it is reachable
            if s[i] != 'z' and best[ord(s[i]) - ord('a') + 1] != -1:
                farthest = best[ord(s[i]) - ord('a') + 1]

            best[ord(s[i]) - ord('a')] = max(best[ord(s[i]) - ord('a')],
                                             farthest)

            # Only 'a' can be a starting point
            if s[i] == 'a':
                ans = max(ans, farthest - i)

        return ans