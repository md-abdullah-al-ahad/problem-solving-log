import string
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        hashmap = {letter: 0 for letter in string.ascii_lowercase}
        for c in s:
            hashmap[c]+=1
        odd_count = 0
        for alph in hashmap:
            if hashmap[alph]%2==1:
                odd_count+=1
        if odd_count>k:
            return False
        return True
