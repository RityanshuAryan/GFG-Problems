class Solution:
# Function to find count of triplets having
# sum less than or equal to val.
    def countTripletsLessThan(self, arr: list[int], val: int) -> int:
        arr.sort()
        n = len(arr)
        ans = 0

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                s = arr[i] + arr[j] + arr[k]

                if s > val:
                    k -= 1
                else:
                    ans += k - j
                    j += 1

        return ans

# Function to return count of triplets
# having sum in range [l, r].
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        return self.countTripletsLessThan(arr, r) - \
               self.countTripletsLessThan(arr, l - 1)