class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = [0]*10005
        ans = []
        for i in range (len(nums)):
            nums[i]=abs(nums[i])
        limit = max(nums)+1
        for num in nums:
            num = abs(num)
            lst[num]+=1
        for i in range (limit):
            while lst[i]!=0:
                ans.append(i*i)
                lst[i]-=1
        return ans
            