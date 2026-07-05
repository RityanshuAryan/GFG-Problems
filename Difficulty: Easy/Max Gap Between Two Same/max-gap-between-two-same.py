class Solution:

    def maxCharGap(self, s: str) -> int:
        # first[i] stores the first index of character ('a' + i)
        first = [-1] * 26
        res = -1

        for i in range(len(s)):
            ch = ord(s[i]) - ord('a')

            if first[ch] == -1:
                # First time seeing this character
                first[ch] = i
            else:
                # Characters between first occurrence and current occurrence
                res = max(res, i - first[ch] - 1)

        return res