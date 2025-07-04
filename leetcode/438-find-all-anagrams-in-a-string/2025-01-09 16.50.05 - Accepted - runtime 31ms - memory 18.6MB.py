import string
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        index = []
        p_dict = {letter: 0 for letter in string.ascii_lowercase}
        s_dict = {letter: 0 for letter in string.ascii_lowercase}
        for c in p:
            p_dict[c] += 1
        
        n, n_p = len(s), len(p)
        if n < n_p:
            return []
        for i in range(n_p):
            s_dict[s[i]] += 1
        if s_dict == p_dict:
            index.append(0)

        i = 1
        j = n_p
        while j < n:
            s_dict[s[i - 1]] -= 1
            s_dict[s[j]] += 1
            if s_dict == p_dict:
                index.append(i)

            i += 1
            j += 1
        
        return index
