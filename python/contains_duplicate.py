"""
Idea: Create a set to remove duplicates and compare that length to the length of the input array.

Time: O(n)
Space: O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
