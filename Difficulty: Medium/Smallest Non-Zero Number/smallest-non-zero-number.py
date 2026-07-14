import math


class Solution:

    # Function to find the number by averaging elements in the array.
    def find(self, arr):

        # Custom round function to mimic C++ round behavior
        def custom_round(x):

            # Mimicking the rounding behavior of C++ where 0.5 rounds away from zero
            if x >= 0:
                return int(math.floor(x + 0.5))
            else:
                return int(math.ceil(x - 0.5))

        num = 0

        # Iterating over the array in reverse order.
        for i in range(len(arr) - 1, -1, -1):

            # Averaging the current element with the previous sum using custom rounding
            num = custom_round((arr[i] + num) / 2.0)
        return num