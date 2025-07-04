# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        i = 0
        while current:
            if i>10000:
                return True
            if current.next == None:
                return False
            i+=1
            current=current.next
        return False