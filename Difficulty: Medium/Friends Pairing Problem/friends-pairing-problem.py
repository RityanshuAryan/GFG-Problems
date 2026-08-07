class Solution:

    def countFriendsPairings(self, n: int) -> int:

        # Base cases f(1) = 1 and f(2) = 2
        a, b = 1, 2
        if n <= 2:
            return n

        for i in range(3, n + 1):

            # Calculate the next value without modular arithmetic
            c = b + (i - 1) * a
            a = b
            b = c

        return c