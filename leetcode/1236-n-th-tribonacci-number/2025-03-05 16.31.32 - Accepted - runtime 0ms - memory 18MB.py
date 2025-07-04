class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1]*40
        def helper(n):
            if n==0 or n==1:
                dp[n]=n
            if n == 2:
                dp[n]=1
            if dp[n]==-1:
                dp[n]=helper(n-1)+helper(n-2)+helper(n-3)
            return dp[n]
        return helper(n)
