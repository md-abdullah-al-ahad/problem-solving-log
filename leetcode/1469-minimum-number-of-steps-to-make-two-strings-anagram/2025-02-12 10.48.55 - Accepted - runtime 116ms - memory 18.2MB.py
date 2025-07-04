class Solution:
    def minSteps(self, s: str, t: str) -> int:
        total = 0
        lst1 = [0]*26
        lst2 = [0]*26
        for c in s:
            lst1[ord(c)-ord('a')]+=1
        for c in t:
            lst2[ord(c)-ord('a')]+=1
        for i in range (26):
            total += abs(lst1[i]-lst2[i])
        return total//2