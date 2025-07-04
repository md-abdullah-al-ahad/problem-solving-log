class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        fact = 9
        decrement = 9
        if n==0:
            return 1
        elif n == 1:
            return 10
        else:
            count = 10
            for i in range (2,n+1):
                fact*=decrement
                decrement -=1
                count += fact
        return count
        
