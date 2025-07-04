class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        hashmap = {}
        for i in range(2**n):
            hashmap[format(i, f'0{n}b')]=0
        for num in nums:
            hashmap[num]+=1
        for key in hashmap:
            if hashmap[key]==0:
                return key
    


        
