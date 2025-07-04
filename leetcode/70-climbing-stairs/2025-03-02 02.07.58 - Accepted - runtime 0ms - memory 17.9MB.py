class Solution:
    def climbStairs(self, n: int) -> int:
        lst = [-1]*46
        def helper(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if lst[n]==-1:
                lst[n]=helper(n-1)+helper(n-2)
            return lst[n]
        return helper(n)
