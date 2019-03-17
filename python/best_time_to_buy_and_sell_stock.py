class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = float("inf")
        
        for price in prices:
            min_so_far = min(min_so_far, price)
            max_profit = max(max_profit, price - min_so_far)
        
        return max_profit
