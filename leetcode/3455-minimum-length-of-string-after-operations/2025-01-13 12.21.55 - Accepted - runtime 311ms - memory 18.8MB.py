import string
class Solution:
    def minimumLength(self, s: str) -> int:
        hash_set = {letter: 0 for letter in string.ascii_lowercase}
        for c in s:
            hash_set[c]+=1
            if hash_set[c]==3:
                hash_set[c]=1
        return sum(hash_set.values())