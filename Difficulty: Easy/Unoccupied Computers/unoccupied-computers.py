class Solution:

    def solve(self, n, s):
        state = [0] * 26  # 0 = not seen, 1 = waiting, 2 = using computer
        occupied = 0
        rejected = 0

        for ch in s:
            idx = ord(ch) - ord('A')

            # first time arrival
            if state[idx] == 0:
                state[idx] = 1

                # assign computer if available
                if occupied < n:
                    occupied += 1
                    state[idx] = 2
                else:
                    rejected += 1  # no computer available

            # departure
            else:
                if state[idx] == 2:
                    occupied -= 1
                state[idx] = 0

        return rejected