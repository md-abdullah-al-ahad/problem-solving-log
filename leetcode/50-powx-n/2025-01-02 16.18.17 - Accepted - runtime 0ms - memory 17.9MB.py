class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        num = n
        if n<0:
            n= -n
        while n != 0:
            if n % 2 == 1:
                res *= x
                n -= 1
            else:
                x *= x
                n //= 2
        if num < 0:
            return 1.0 / res
        else:
            return res
