class Solution:
    def reverse(self, x: int) -> int:
        max_value = 2**31 - 1
        ans = 0
        if x<0:
            sign = -1
            x=abs(x)
        else:
            sign = 1
        while x!=0:
            digit = x%10
            if ans > (max_value-digit)//10:
                return 0
            ans = ans*10 + digit
            x//=10
        return ans*sign
                
