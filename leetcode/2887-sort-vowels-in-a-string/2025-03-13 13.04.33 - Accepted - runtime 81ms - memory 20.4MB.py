class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        v = ""
        for c in s:
            if c in vowels:
                v += c
        v = sorted(v)
        i = 0
        lst = []
        for c in s:
            if c in vowels:
                lst.append(v[i])
                i += 1
            else:
                lst.append(c)
        return "".join(lst)
