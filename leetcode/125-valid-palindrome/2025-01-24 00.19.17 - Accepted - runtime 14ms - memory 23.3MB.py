class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        n = len(s)
        i = 0
        while(i<(n//2)):
            if s[i]!=s[n-i-1]:
                return False
            i+=1
        return True