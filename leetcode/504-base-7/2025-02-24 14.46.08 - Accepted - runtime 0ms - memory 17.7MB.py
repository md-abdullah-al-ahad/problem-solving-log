class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = ""
        sign = False
        if num<0:
            sign = True
        num = abs(num)
        while num!=0:
            rem = num % 7
            ans+=str(rem)
            num = num // 7
        if sign:
            ans+="-"
        return ans[::-1]