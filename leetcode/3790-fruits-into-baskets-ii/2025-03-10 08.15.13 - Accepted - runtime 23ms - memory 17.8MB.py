class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        lst = [0]*len(baskets)
        total = 0
        for fruit in fruits:
            i = 0
            for i in range (len(baskets)):
                if baskets[i]>=fruit and lst[i]==0:
                    total+=1
                    lst[i]=1
                    break
        return len(fruits)-total
            