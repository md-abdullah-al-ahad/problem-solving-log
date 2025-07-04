class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        j = num // 3
        i = j - 1
        k = j + 1
        if i+j+k == num:
            return [i,j,k]
        return []