class Solution:

    def findWays(self, grid):
        MOD = int(1e9 + 7)
        n = len(grid)

        # Arrays to store the data of the "next" row below (i + 1)
        nextWays = [0] * n

        # Initialize as unreachable (-1)
        nextAdv = [-1] * n

        # Iterate backwards from the bottom row to the top row
        for i in range(n - 1, -1, -1):
            currWays = [0] * n
            currAdv = [-1] * n

            for j in range(n - 1, -1, -1):
                # Base Case: Bottom-right cell (The Exit)
                if i == n - 1 and j == n - 1:
                    currWays[j] = 1
                    currAdv[j] = grid[i][j]
                    continue

                totalWays = 0
                maxAdventure = -1
                cellValue = grid[i][j]

                # Option 1: Move Right (Valid for cell values 1 and 3)
                if cellValue == 1 or cellValue == 3:
                    # Check if right neighbor is within boundaries and reachable
                    if j + 1 < n and currAdv[j + 1] != -1:
                        totalWays = (totalWays + currWays[j + 1]) % MOD
                        maxAdventure = max(maxAdventure,
                                           grid[i][j] + currAdv[j + 1])

                # Option 2: Move Down (Valid for cell values 2 and 3)
                if cellValue == 2 or cellValue == 3:
                    # Check if bottom neighbor is within boundaries and reachable
                    if i + 1 < n and nextAdv[j] != -1:
                        totalWays = (totalWays + nextWays[j]) % MOD
                        maxAdventure = max(maxAdventure,
                                           grid[i][j] + nextAdv[j])

                currWays[j] = totalWays
                currAdv[j] = maxAdventure  # Remains -1 if no valid path exists

            # Move row states upwards efficiently
            nextWays = currWays
            nextAdv = currAdv

        # Results are aggregated back at the entry point (0, 0)
        finalPaths = nextWays[0]
        finalAdv = 0 if nextAdv[0] == -1 else nextAdv[0]

        return [finalPaths, finalAdv]