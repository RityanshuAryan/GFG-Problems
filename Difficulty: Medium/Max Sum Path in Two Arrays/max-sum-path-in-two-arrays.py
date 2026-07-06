class Solution:

    def maxPathSum(self, a, b):
        i, j = 0, 0
        result, sum1, sum2 = 0, 0, 0
        m, n = len(a), len(b)

        # Using two pointers to iterate over two arrays
        while i < m and j < n:

            # if a is smaller than b, increasing a and adding its value to sum1
            if a[i] < b[j]:
                sum1 += a[i]
                i += 1

            # if b is smaller than a, increasing b and adding its value to sum2
            elif a[i] > b[j]:
                sum2 += b[j]
                j += 1

            # if a equals b, checking the maximum sum obtained from both the arrays
            # updating result and sum1 and sum2 are again changed to zero
            else:
                result += max(sum1, sum2)
                sum1 = 0
                sum2 = 0
                while i < m and j < n and a[i] == b[j]:
                    result += a[i]
                    i += 1
                    j += 1

        # if jth pointer reaches end
        while i < m:
            sum1 += a[i]
            i += 1

        # if ith pointer reaches end
        while j < n:
            sum2 += b[j]
            j += 1

        # last maximum sum to be added after the end of the loop
        result += max(sum1, sum2)

        return result