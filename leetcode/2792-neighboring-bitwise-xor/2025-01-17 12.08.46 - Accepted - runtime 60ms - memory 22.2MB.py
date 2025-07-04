class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        i, j = 0, 0
        for bit in derived:
            if bit == 1:
                if j == 1:
                    j = 0
                else:
                    j = 1
        return i == j
