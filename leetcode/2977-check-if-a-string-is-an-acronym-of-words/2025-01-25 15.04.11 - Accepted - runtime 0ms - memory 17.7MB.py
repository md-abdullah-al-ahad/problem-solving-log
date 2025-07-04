class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words)!=len(s):
            return False
        pointer = 0
        for word in words:
            if word[0]!=s[pointer]:
                return False
            else:
                pointer+=1
        return True