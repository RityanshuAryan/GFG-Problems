class Solution:

    def maxAmount(self, arr, k):
        mod = 1000000007
        n = len(arr)

        # Convert arr into a max heap by inverting the values
        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)

        ans = 0
        while k > 0 and max_heap:

            # Get the largest element (smallest in the inverted max heap)
            x = -heapq.heappop(max_heap)
            ans = (ans + x) % mod
            x -= 1
            k -= 1
            if x > 0:
                # Push the updated value back into the heap
                heapq.heappush(max_heap, -x)

        return ans