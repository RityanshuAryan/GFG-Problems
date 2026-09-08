class Solution:

        # Function to check if word exists starting from (row, col)
        # in all 8 possible directions
        def search2D(self, mat, row, col, word, dx, dy):

            n = len(mat)  # number of rows
            m = len(mat[0])  # number of columns

            # First character must match
            if mat[row][col] != word[0]:
                return False

            length = len(word)  # length of word to search

            # Try all 8 directions
            for dir in range(8):

                # move one step in current direction
                r = row + dx[dir]
                c = col + dy[dir]

                k = 1  # already matched first character

                # check remaining characters of word
                while k < length:

                    # boundary check
                    if r < 0 or r >= n or c < 0 or c >= m:
                        break

                    # character mismatch
                    if mat[r][c] != word[k]:
                        break

                    # move further in same direction
                    r += dx[dir]
                    c += dy[dir]
                    k += 1

                # if full word matched
                if k == length:
                    return True

            # word not found in any direction
            return False

        # Function to find all starting positions where word is found
        def searchWord(self, mat, word):

            n = len(mat)  # number of rows
            m = len(mat[0])  # number of columns

            # 8 directions: up, down, left, right, and diagonals
            dx = [-1, -1, -1, 0, 0, 1, 1, 1]
            dy = [-1, 0, 1, -1, 1, -1, 0, 1]

            ans = []  # store result coordinates

            # try every cell as starting point
            for i in range(n):
                for j in range(m):

                    # if word found starting here, store position
                    if self.search2D(mat, i, j, word, dx, dy):
                        ans.append([i, j])

            return ans