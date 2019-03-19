"""Bit Manipulation

Idea: Logical AND every Least Significant Bit (LSB) with 0x1.

Time - O(n)* 
It runs linearly with the number of input bits, though the input is 32b or 64b so
it is essentially constant.

Space - O(1)
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hamming_weight = 0
        while n != 0:
            hamming_weight += (n & 1)  # pull of first bit
            n = n >> 1  # remove bit we just checked
        return hamming_weight
