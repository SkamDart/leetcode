"""
Idea: Our missing number is the difference between 
    \summation_{i = 0}^{n} i which has a closed form solution of (n * (n + 1)) / 2
    and the sum of nums
    
    
Time - O(n)
Space - O(1)
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return ((n * (n + 1)) / 2) - sum(nums)
