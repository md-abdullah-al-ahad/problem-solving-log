class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        one_d=[]
        for numbers in matrix:
            for number in numbers:
                one_d.append(number)
        left = 0
        right = len(one_d) -1
        while left<=right:
            mid = left + (right-left)//2
            if one_d[mid] == target:
                return True
            elif one_d[mid]<target:
                left = mid + 1
            else:
                right = mid - 1
        return False