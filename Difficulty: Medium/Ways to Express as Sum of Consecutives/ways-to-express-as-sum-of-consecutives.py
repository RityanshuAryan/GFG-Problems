class Solution:

    def getCount(self, n):
        count = 0

        # k represents the number of terms in our consecutive sequence.
        # we need 2 or more consecutive numbers, so k starts at 2.
        k = 2
        while True:

            baseSum = (k * (k - 1)) // 2

            # if baseSum is greater than or equal to n, a valid sequence
            # of length k is impossible.
            if baseSum >= n:
                break

            # check if (n - baseSum) is perfectly divisible by k
            # if the remainder is 0, a valid starting number 'a' exists
            if (n - baseSum) % k == 0:
                count += 1

            k += 1

        return count