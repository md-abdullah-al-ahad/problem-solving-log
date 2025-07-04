import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1
        heap = []
        for key, value in hashmap.items():
            heapq.heappush(heap, (-value, key))
        ans = ""
        while heap:
            value, key = heapq.heappop(heap)
            ans += key * (-value)
        return ans
