class Solution:

        def maxProduct(self, arr: list[int], k: int) -> int:

            n = len(arr)

            # Sort the array.
            arr.sort()

            # Store the maximum product.
            product = 1

            # If the largest element is 0 and k is odd.
            if arr[n - 1] == 0 and (k & 1):
                return 0

            # If all elements are non-positive and k is odd.
            if arr[n - 1] <= 0 and (k & 1):

                for i in range(n - 1, n - k - 1, -1):
                    product *= arr[i]

                return product

            left = 0
            right = n - 1

            # Include the largest positive element if k is odd.
            if k & 1:
                product *= arr[right]
                right -= 1
                k -= 1

            # Process the remaining elements in pairs.
            k //= 2

            for _ in range(k):

                leftProduct = arr[left] * arr[left + 1]
                rightProduct = arr[right] * arr[right - 1]

                # Choose the better pair.
                if leftProduct > rightProduct:
                    product *= leftProduct
                    left += 2
                else:
                    product *= rightProduct
                    right -= 2

            # Return the maximum product.
            return product