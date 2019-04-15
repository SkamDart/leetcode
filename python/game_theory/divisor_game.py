# https://leetcode.com/contest/weekly-contest-132/problems/divisor-game/
class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        elif N & 1 == 0:
            return True
        else:
            return False
