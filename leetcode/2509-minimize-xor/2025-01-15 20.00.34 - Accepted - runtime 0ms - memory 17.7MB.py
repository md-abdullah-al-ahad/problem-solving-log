class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def set_bits(n):
            ans = 0
            while n > 0:
                ans += 1 & n
                n = n >> 1
            return ans
        count1,count2 = set_bits(num1),set_bits(num2)
        i = 0
        while count1>count2:
            if num1 & (1<<i):
                count1-=1
                num1 = num1^(1<<i)
            i+=1
        while count1<count2:
            if num1 & (1<<i) == 0:
                count1+=1
                num1 = num1 | (1<<i)
            i+=1
        return num1
