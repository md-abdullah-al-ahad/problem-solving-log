class Solution:
    lst = [-1]*46
    def climbStairs(self, n: int) -> int:
        if n == 1:
            self.lst[n] = 1
        elif n == 2:
            self.lst[n] = 2
        if self.lst[n] == -1:
            self.lst[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.lst[n]
