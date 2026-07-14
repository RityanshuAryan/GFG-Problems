class Solution:

    def bitonic(self, arr):
        n = len(arr)

        # if arr is empty
        if n == 0:
            return 0

        # initializing max_len
        maxLen = 1

        start = 0
        nextStart = 0

        j = 0
        while j < n - 1:

            # look for end of ascent
            while j < n - 1 and arr[j] <= arr[j + 1]:
                j += 1

            # look for end of descent
            while j < n - 1 and arr[j] >= arr[j + 1]:

                # adjusting nextStart;
                # this will be necessarily executed at least once,
                # when we detect the start of the descent
                if j < n - 1 and arr[j] > arr[j + 1]:
                    nextStart = j + 1

                j += 1

            # updating maxLen, if required
            maxLen = max(maxLen, j - (start - 1))

            start = nextStart

        return maxLen