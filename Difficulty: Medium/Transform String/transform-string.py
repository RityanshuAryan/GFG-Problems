class Solution:
    
    def transform(self, s1, s2):
        if len(s1) != len(s2):
            return -1

        freq = {}

        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in s2:
            if ch in freq:
                freq[ch] -= 1
            else:
                return -1

        for val in freq.values():
            if val != 0:
                return -1

        i = len(s1) - 1
        j = len(s2) - 1

        operations = 0

        while i >= 0 and j >= 0:

            while i >= 0 and s1[i] != s2[j]:
                i -= 1
                operations += 1

            i -= 1
            j -= 1

        return operations