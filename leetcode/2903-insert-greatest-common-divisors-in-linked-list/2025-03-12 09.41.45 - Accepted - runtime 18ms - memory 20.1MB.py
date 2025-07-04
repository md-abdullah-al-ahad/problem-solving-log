# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        current = head
        while current and current.next:
            g = gcd(current.val, current.next.val)
            new_node = ListNode(g)
            new_node.next = current.next
            current.next = new_node
            current = current.next.next
        return head
