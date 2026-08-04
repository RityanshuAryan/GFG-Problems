class Solution:

    def countPairs(self, arr: list[int], k: int) -> int:

        # Sorting the array
        arr.sort()

        # Start index
        s = 0

        # Total count of pairs
        total = 0

        # Traverse the sorted array
        for i in range(1, len(arr)):

            # Find the number of elements between i and s
            # with a difference greater than or equal to k
            while s < i and arr[i] - arr[s] >= k:
                s += 1

            # Add the count of such pairs to the total
            total += i - s

        return total