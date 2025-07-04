class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        hashmap = [0]*len(nums)
        for i in range (len(nums)-1):
            if nums[i]&1 == nums[i+1]&1:
                hashmap[i]+=1
        for i in range (1,len(hashmap)):
            hashmap[i]=hashmap[i]+hashmap[i-1]
        for query in queries:
            if query[0] == query[1]:
                ans.append(True)
                continue
            if query[0]==0:
                if hashmap[query[1]-1]>0:
                    ans.append(False)
                else:
                    ans.append(True)
            else:
                if hashmap[query[1]-1]-hashmap[query[0]-1]>0:
                    ans.append(False)
                else:
                    ans.append(True)
        return ans
