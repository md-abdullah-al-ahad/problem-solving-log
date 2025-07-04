class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst = [0]*len(nums)
        for num in nums:
            if lst[num]!=0:
                return num
            else:
                lst[num]+=1
        
        
            