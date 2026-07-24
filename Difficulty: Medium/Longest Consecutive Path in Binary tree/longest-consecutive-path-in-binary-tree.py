res = 0


class Solution:

    #Utility function to find the length of the longest consecutive sequence
    def longConsUtil(self, root, curlength, expected):

        #if the root is None, return
        if root is None:
            return

        #if the value of the root is equal to the expected value,
        #increment the current length
        if root.data == expected:
            curlength += 1

        #if the value of the root is not equal to the expected value,
        #reset the current length to 1
        else:
            curlength = 1

        #update the maximum length of consecutive sequence
        global res
        res = max(res, curlength)

        #recursive call for the left and right subtree
        self.longConsUtil(root.left, curlength, root.data + 1)
        self.longConsUtil(root.right, curlength, root.data + 1)

    #Function to find the length of the longest consecutive sequence
    def longestConsecutive(self, root):

        #if the root is None, return 0
        if root is None:
            return -1

        #initialize the maximum length to 0
        global res
        res = 0

        #utility function to find the length of the longest consecutive sequence
        self.longConsUtil(root, 0, root.data)

        #if the maximum length is less than or equal to 1, return -1
        if (res <= 1):
            return -1

        #return the maximum length of consecutive sequence
        return res