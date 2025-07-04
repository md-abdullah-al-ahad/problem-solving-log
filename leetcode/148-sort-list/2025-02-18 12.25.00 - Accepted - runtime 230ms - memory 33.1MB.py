# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from sortedcontainers import SortedList
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = SortedList()
        current = head
        while current:
            lst.add(current.val)
            current= current.next
        current = head
        i = 0
        while current:
            current.val = lst[i]
            i+=1
            current= current.next
        return head