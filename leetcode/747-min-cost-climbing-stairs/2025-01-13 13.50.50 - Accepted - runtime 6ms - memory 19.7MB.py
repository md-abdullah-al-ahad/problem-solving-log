from typing import List


class Solution:
    def __init__(self):
        self.dp = [-1] * 1001

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def solve(n: int) -> int:
            if n == 0:
                self.dp[0] = cost[0]
                return self.dp[0]
            elif n == 1:
                self.dp[1] = cost[1]
                return self.dp[1]
            if self.dp[n] != -1:
                return self.dp[n]
            self.dp[n] = min(solve(n - 1), solve(n - 2)) + (
                cost[n] if n < len(cost) else 0
            )
            return self.dp[n]

        return min(solve(n - 1), solve(n - 2))
