class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total = 0
        i = j = 0
        while j<len(nums):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
                total+=1
            j+=1
        return total
        
        