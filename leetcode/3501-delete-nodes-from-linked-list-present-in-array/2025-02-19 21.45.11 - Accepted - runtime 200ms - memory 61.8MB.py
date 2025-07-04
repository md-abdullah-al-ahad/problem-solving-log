# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        lst = [0]*100001
        for num in nums:
            lst[num]+=1
        ret_dummy = dummy = ListNode(0)
        current = head
        while current:
            if lst[current.val]==0:
                new_node = ListNode(current.val)
                dummy.next = new_node
                dummy = dummy.next
            current = current.next
        return ret_dummy.next