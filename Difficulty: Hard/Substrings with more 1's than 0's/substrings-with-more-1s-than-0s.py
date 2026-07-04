class Solution:

    # Function to count the number of substrings
    def countSubstring(self, s):

        n = len(s)

        ans = 0
        zero = n
        minus = 0

        mp = [0] * (2 * n + 5)

        cur = zero

        # Loop through the string to determine the number of zeros and minuses
        for ch in s:

            if ch == '0':
                cur -= 1
            else:
                cur += 1

            if cur <= zero:
                minus += 1

            mp[cur] += 1

        # Loop through the string again to count the number of valid substrings
        for i in range(n):

            ans += (n - i - minus)

            if s[i] == '1':

                mp[zero + 1] -= 1

                zero += 1

                minus += mp[zero]

            else:

                mp[zero - 1] -= 1

                zero -= 1

                minus -= 1

                minus -= mp[zero + 1]

        return ans