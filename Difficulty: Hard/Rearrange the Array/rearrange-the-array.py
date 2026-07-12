class Solution:
    MOD = 1000000007

    def modPow(self, x: int, y: int) -> int:
        res = 1
        while y:
            if y & 1:
                res = (res * x) % self.MOD
            x = (x * x) % self.MOD
            y >>= 1
        return res

    def minOperations(self, b):
        n = len(b)
        vis = [False] * n
        cycles = []

        # Find cycle lengths
        for i in range(n):
            if not vis[i]:
                length = 0
                cur = i

                while not vis[cur]:
                    vis[cur] = True

                    # 1-based -> 0-based
                    cur = b[cur] - 1
                    length += 1

                cycles.append(length)

        # Sieve for primes up to n
        spf = list(range(n + 1))

        for i in range(2, int(n**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, n + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        maxPower = {}

        # Factorize each cycle length
        for length in cycles:
            freq = {}

            while length > 1:
                p = spf[length]
                cnt = 0

                while length % p == 0:
                    length //= p
                    cnt += 1

                freq[p] = cnt

            for key, value in freq.items():
                if key in maxPower:
                    maxPower[key] = max(maxPower[key], value)
                else:
                    maxPower[key] = value

        res = 1

        # Construct LCM modulo MOD
        for key, value in maxPower.items():
            res = (res * self.modPow(key, value)) % self.MOD

        return res