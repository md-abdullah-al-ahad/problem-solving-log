class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list_s = [0]*26
        list_t = [0]*26
        for c in s:
            list_s[ord(c)-ord('a')]+=1
        for c in t:
            list_t[ord(c)-ord('a')]+=1
        for i in range (26):
            if list_s[i]!=list_t[i]:
                return chr(ord('a') + i)