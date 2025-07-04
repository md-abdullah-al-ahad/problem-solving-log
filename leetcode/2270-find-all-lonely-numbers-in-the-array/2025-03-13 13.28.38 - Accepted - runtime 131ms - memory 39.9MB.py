class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        lst = []
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        for num in nums:
            if hashmap[num] == 1 and num - 1 not in hashmap and num + 1 not in hashmap:
                lst.append(num)
        return lst
