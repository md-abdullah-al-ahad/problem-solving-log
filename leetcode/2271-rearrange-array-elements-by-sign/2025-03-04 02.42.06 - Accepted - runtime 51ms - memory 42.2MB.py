class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        ans = [0]*len(nums)
        for num in nums:
            if num>0:
                ans[i]=num
                i+=2
        for num in nums:
            if num<0:
                ans[j]=num
                j+=2
        return ans
