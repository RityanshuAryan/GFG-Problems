class Solution:

    def countMinOperations(self, arr):
        # Sort the array to process elements in descending order
        arr.sort()
        ans = 0

        while True:
            # Flag to check if all elements are zero
            allZero = True

            # Iterate from the largest to the smallest element
            for i in range(len(arr) - 1, -1, -1):
                if arr[i] % 2 == 1:
                    # Decrement odd elements
                    arr[i] -= 1
                    # Count the decrement operation
                    ans += 1
                if arr[i] != 0:
                    # Check if the element is non-zero
                    allZero = False
                # Halve the element
                arr[i] //= 2

            # Break if all elements are zero
            if allZero:
                break
            # Count the halving operation
            ans += 1

        # Return the total number of operations
        return ans