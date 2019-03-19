"""Dynamic Programming

Idea - Define a recursive function then memoize the recurrence to optimize for time complexity
    Let f(n) be the number of distinct ways you can climb up to the nth stair

    f(1) = 1
    f(2) = 2
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        a = 1
        b = 1
        for _ in range(n - 1):
            a, b = a + b, a
        return a
