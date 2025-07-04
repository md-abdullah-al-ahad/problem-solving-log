from collections import Counter
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        total = set()
        freq = Counter()
        lst = {}
        ans = []
        for query in queries:
            index, value = query
            if index in lst:
                old_value = lst[index]
                freq[old_value] -= 1
                if freq[old_value] == 0:
                    total.remove(old_value)
            lst[index] = value
            freq[value] += 1
            if freq[value] == 1:
                total.add(value)
            ans.append(len(total))
        return ans
