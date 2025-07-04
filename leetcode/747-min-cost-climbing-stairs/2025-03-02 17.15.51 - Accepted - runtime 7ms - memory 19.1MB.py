class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        lst = [-1]*(n+1)
        def helper(n):
            if n <=1:
                lst[n]=cost[n]
            if lst[n]==-1:
                lst[n]= min(helper(n - 1), helper(n - 2)) + cost[n]
            return lst[n]
        return min(helper(n - 1), helper(n - 2))