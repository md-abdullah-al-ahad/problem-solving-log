class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        sub_set = set()
        ans_set = set()
        i = 0
        j = 10
        while j <= len(s):
            sub_string = s[i:j]
            if sub_string in sub_set:
                ans_set.add(sub_string)
            else:
                sub_set.add(sub_string)
            i += 1
            j += 1
        return list(ans_set)
