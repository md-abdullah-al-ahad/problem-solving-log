# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        length = 0
        current = head
        while current:
            length+=1
            current=current.next
        current = head
        for i in range (length-1,-1,-1):
            if current.val == 1:
                ans += pow(2,i)
            current = current.next
        return ans