class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        index = p.index('*')
        left = p[:index]
        right = p[index+1:]
        i = s.find(left)
        j = s.rfind(right)
        if i != -1 and j!=-1 and i+len(left)<=j:
            return True
        return False
