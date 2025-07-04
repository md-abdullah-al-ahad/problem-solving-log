# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = None
        while l1:
            temp = l1.next
            l1.next = node1
            node1 = l1
            l1 = temp
        node2= None
        while l2:
            temp = l2.next
            l2.next = node2
            node2 = l2
            l2 = temp
        carry = 0
        ans = None
        while node1 or node2 or carry:
            total = carry
            if node1:
                total+=node1.val
                node1 = node1.next
            if node2:
                total+=node2.val
                node2 = node2.next
            new_node = ListNode(total%10)
            carry = total//10
            new_node.next = ans
            ans = new_node
        return ans