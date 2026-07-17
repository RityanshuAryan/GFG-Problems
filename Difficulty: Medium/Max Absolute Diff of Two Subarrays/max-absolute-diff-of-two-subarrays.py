class Solution:

    # Builds max subarray sums from left side.
    # leftMax[i] = maximum subarray sum within arr[0...i]
    def buildLeftMax(self, arr):
        n = len(arr)

        leftMax = [0] * n

        curr = arr[0]
        best = arr[0]

        leftMax[0] = best

        for i in range(1, n):
            curr = max(arr[i], curr + arr[i])  # Kadane
            best = max(best, curr)

            leftMax[i] = best

        return leftMax

    # Builds max subarray sums from right side
    # rightMax[i] = maximum subarray sum within arr[i...n-1]
    def buildRightMax(self, arr):
        n = len(arr)

        rightMax = [0] * n

        curr = arr[n - 1]
        best = arr[n - 1]

        rightMax[n - 1] = best

        for i in range(n - 2, -1, -1):
            curr = max(arr[i], curr + arr[i])
            best = max(best, curr)

            rightMax[i] = best

        return rightMax

    def maxDiffSubArrays(self, arr):
        n = len(arr)

        # Maximum subarray sums
        leftMax = self.buildLeftMax(arr)
        rightMax = self.buildRightMax(arr)

        # Invert array to compute minimum subarray sums
        inverted = [-x for x in arr]

        # Maximum on inverted = Minimum on original
        leftMin = self.buildLeftMax(inverted)
        rightMin = self.buildRightMax(inverted)

        # Convert back
        leftMin = [-x for x in leftMin]
        rightMin = [-x for x in rightMin]

        ans = float('-inf')

        # Try every partition
        for i in range(n - 1):

            # Case 1:
            # max(left) - min(right)
            option1 = abs(leftMax[i] - rightMin[i + 1])

            # Case 2:
            # min(left) - max(right)
            option2 = abs(leftMin[i] - rightMax[i + 1])
            ans = max(ans, option1, option2)
        return ans