class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        ans = []
        highest = -1
        for key in hashmap:
            if hashmap[key] > highest:
                highest = hashmap[key]
        for i in range(highest):
            row = []
            for key in hashmap:
                if hashmap[key] > 0:
                    row.append(key)
                    hashmap[key] -= 1
            ans.append(row)
        return ans
