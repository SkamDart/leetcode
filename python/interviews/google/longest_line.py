class Solution(object):
        
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0 or len(M[0]) == 0:
            return 0
        m = len(M)
        n = len(M[0])
        memo = [[[0] * 4 for _ in range(n)] for _ in range(m)]
        longest_line = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    memo[i][j][0] = 1 + memo[i][j - 1][0] if j > 0 else 1
                    memo[i][j][1] = 1 + memo[i - 1][j][1] if i > 0 else 1
                    memo[i][j][2] = 1 + memo[i - 1][j - 1][2] if i > 0 and j > 0 else 1
                    memo[i][j][3] = 1 + memo[i - 1][j + 1][3] if i > 0 and j < n - 1 else 1
                    longest_line = max(longest_line, *memo[i][j])
        return longest_line
