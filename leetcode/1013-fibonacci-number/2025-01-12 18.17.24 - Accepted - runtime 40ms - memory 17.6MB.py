class Solution:
    lst = [-1]*31
    def fib(self, n: int) -> int:
        if n==0:
            self.lst[n]=0
        if n == 1:
            self.lst[n]=1
        if self.lst[n]==-1:
            self.lst[n] = self.fib(n-1) + self.fib(n-2)
        return self.lst[n]