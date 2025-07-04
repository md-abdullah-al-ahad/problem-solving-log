class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lst = []
        totalpivot = 0
        for num in nums:
            if num < pivot:
                lst.append(num)
            if num == pivot:
                totalpivot+=1
        while totalpivot:
            lst.append(pivot)
            totalpivot-=1
        for num in nums:
            if num > pivot:
                lst.append(num)
        return lst