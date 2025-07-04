class Solution:
    def isPalindrome(self, x: int) -> bool:
        total = 0
        num = x
        if x<0:
            return False
        else:
            while x!=0:
                rem = x%10
                total = total*10+rem
                x//=10
        return total == num