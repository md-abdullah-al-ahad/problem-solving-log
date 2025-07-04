class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        lst = [-1]*1001
        def helper(n):
            if n <=1:
                lst[n]=cost[n]
            if lst[n]==-1:
                lst[n]= min(helper(n - 1), helper(n - 2)) + (cost[n] if n < len(cost) else 0)
            return lst[n]
        return min(helper(n - 1), helper(n - 2))