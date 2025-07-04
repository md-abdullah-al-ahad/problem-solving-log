class Solution:
    def fib(self, n: int) -> int:
        lst = [-1]*31
        def helper(n):
            if n==0:
                lst[n]=0
            if n == 1:
                lst[n]=1
            if lst[n]==-1:
                lst[n] = helper(n-1) + helper(n-2)
            return lst[n]
        return helper(n)