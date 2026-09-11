class Solution:

    def sameMod(self, arr):
        n = len(arr)

        g = 0

        # Compute the GCD of all differences.
        for i in range(1, n):
            g = self.gcd(g, abs(arr[i] - arr[0]))

        # If all elements are equal, infinitely many values of k exist.
        if g == 0:
            return -1

        cnt = 0

        # Count all positive divisors of the GCD.
        for i in range(1, int(g**0.5) + 1):
            if g % i == 0:
                cnt += 1

                if i != g // i:
                    cnt += 1

        return cnt

    def gcd(self, a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a