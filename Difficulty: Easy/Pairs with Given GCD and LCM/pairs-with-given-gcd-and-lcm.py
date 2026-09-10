def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class Solution:

        def pairCount(self, x, y):
            n, res = 0, 0

            # lcm must be divisible by gcd, else no pair exists
            if y % x == 0:
                n = y // x

            # if n is 1, the only pair is (x, x)
            if n == 1:
                res = 1

            # find coprime factor pairs (i, n/i) of n
            i = 1
            while i * i <= n:
                if n % i == 0:
                    j = n // i

                    # both (x*i, x*j) and (x*j, x*i) are valid
                    # only if i and j are coprime (gcd = 1)
                    if i != j and gcd(x * i, x * j) == x:
                        res += 2
                i += 1

            return res