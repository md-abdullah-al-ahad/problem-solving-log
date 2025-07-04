class Solution:
    lst = [-1] * 38
    def tribonacci(self, n: int) -> int:
        if self.lst[n] != -1:
            return self.lst[n]
        if n == 0:
            self.lst[n] = 0
        elif n == 1 or n == 2:
            self.lst[n] = 1
        else:
            self.lst[n] =self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.lst[n]
