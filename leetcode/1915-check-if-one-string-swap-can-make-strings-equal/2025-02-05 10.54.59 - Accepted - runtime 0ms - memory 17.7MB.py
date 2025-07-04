class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        lst_s1 = [0]*26
        lst_s2 = [0]*26
        total_diff = 0
        for i in range (len(s1)):
            lst_s1[ord(s1[i])-ord('a')]+=1
            lst_s2[ord(s2[i])-ord('a')]+=1
            if s1[i]!=s2[i]:
                total_diff+=1
        if lst_s1!=lst_s2 or total_diff>2:
            return False
        return True
        