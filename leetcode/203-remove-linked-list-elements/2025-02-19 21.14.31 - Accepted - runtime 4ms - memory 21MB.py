# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ret_dummy = dummy = ListNode(0)
        current = head
        while current:
            if current.val != val:
                new_node = ListNode(current.val)
                dummy.next = new_node
                dummy = dummy.next
            current = current.next
        return ret_dummy.next
        