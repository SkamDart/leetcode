  def minCostClimbingStairs(self, cost: List[int]) -> int:
      previous_min = 0
      current_min = 0
      for value in reversed(cost):
          current_min, previous_min = value + min(previous_min, current_min), current_min
      return min(previous_min, current_min)
