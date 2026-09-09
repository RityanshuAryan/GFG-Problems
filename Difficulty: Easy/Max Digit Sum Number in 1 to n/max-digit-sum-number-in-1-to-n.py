class Solution:

        def findMax(self, n):
            s = str(n)
            d = len(s)

            totalSum = 0
            for ch in s:
                totalSum += int(ch)

            ans = n
            bestSum = totalSum

            p = 1
            suffixSum = 0

            # Traverse digits from right to left.
            for i in range(d - 1, -1, -1):
                digit = int(s[i])
                suffixSum += digit

                if digit > 0:
                    # Form the candidate by decreasing the current digit and
                    # making all digits to its right equal to 9.
                    cand = (n // (p * 10)) * (p * 10)
                    cand += (digit - 1) * p
                    cand += p - 1

                    digitsRight = d - i - 1

                    # Compute the candidate's digit sum in O(1).
                    curSum = totalSum - suffixSum + (digit - 1) + 9 * digitsRight

                    # Keep the number with the maximum digit sum.
                    if curSum > bestSum or (curSum == bestSum and cand > ans):
                        bestSum = curSum
                        ans = cand

                p *= 10

            return ans