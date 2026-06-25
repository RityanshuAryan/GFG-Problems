class Solution:

    def solve(self, n, current_digit, current_num, ans):

        # Base case: When we have added n digits, store the number
        if n == 0:
            ans.append(current_num)
            return

        # Next digit must be strictly greater than current_digit
        for i in range(current_digit + 1, 10):
            self.solve(n - 1, i, current_num * 10 + i, ans)

    def increasingNumbers(self, n):
        ans = []

        # Edge case: n = 1 is the only time 0 is included
        if n == 1:
            for i in range(10):
                ans.append(i)
            return ans
        elif n > 9:
            return ans

        # For n > 1, the first digit must be between 1 and 9
        for i in range(1, 10):
            self.solve(n - 1, i, i, ans)

        return ans