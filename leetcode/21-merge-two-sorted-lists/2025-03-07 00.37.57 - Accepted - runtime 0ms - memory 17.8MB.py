class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        head = ListNode(0)  # A dummy node to simplify the merge logic
        ans = head  # This will be the start of the merged list

        # Merge both lists as long as both are not empty
        while current1 and current2:
            if current1.val < current2.val:
                head.next = current1
                current1 = current1.next
            else:
                head.next = current2
                current2 = current2.next
            head = head.next
        if current1:
            head.next = current1
        if current2:
            head.next = current2

        return ans.next
