# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        current = head
        while current:
            n+=1
            current = current.next
        current = head
        for i in range (n):
            if i == k - 1:
                n1 = current
            if i == n-k:
                n2 = current
            current = current.next
        temp = n1.val
        n1.val = n2.val
        n2.val = temp
        return head
