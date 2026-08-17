class Solution:
    def minProd(self, arr):
        neg = 0
        zero = 0
        prod = 1
        mn_neg_abs = float('inf')
        mn_pos = float('inf')

        for x in arr:
            if x == 0:
                zero += 1
                continue

            prod *= x

            if x < 0:
                neg += 1
                mn_neg_abs = min(mn_neg_abs, abs(x))
            else:
                mn_pos = min(mn_pos, x)

        # All elements are zero
        if neg == 0 and mn_pos == float('inf'):
            return 0

        # If there is at least one negative number
        if neg > 0:
            # Odd number of negatives gives minimum product directly
            if neg % 2 == 1:
                return prod

            # Even number of negatives: remove the negative with smallest abs value
            return prod // (-mn_neg_abs)

        # No negative numbers
        if zero > 0:
            return 0

        # Only positive numbers
        return mn_pos