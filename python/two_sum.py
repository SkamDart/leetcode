"""Dynamic Programming

Idea: Remember what values we need to find i.e. (target - values[i]) for all i such that 0 <= i < n

Time - O(n)
Space - O(n)
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def make_inverses(values, k):
            return {target - num:idx for idx, num in enumerate(nums)}

        inverses = make_inverses(nums, target)
        
        for idx, num in enumerate(nums):
            if num in inverses and idx != inverses[num]:
                return [idx, inverses[num]]
