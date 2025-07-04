class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        n = n*n
        if w*n <=maxWeight:
            return n
        else:
            return maxWeight//w
        