class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        total = 0
        for word in words:
            if word[:len(pref)]==pref:
                total+=1
        return total