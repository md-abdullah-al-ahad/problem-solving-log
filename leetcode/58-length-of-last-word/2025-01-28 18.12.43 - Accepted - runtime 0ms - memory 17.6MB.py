class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        n = len(s)
        total = 0
        for i in range (n-1,-1,-1):
            if s[i] == " ":
                break
            else:
                total+=1
        return total
