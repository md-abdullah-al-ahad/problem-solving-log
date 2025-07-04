class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        number = []
        current = head
        while current:
            number.append(current.val)
            current = current.next
        number.reverse()
        carry = 0
        for i in range(len(number)):
            number[i] = number[i] * 2 + carry
            if number[i] >= 10:
                number[i] %= 10
                carry = 1
            else:
                carry = 0
        if carry:
            number.append(1)
        current = head
        i = 0
        number.reverse()
        while current:
            current.val = number[i]
            i += 1
            current = current.next
        if i < len(number):
            new_node = ListNode(number[i])
            current = head
            while current and current.next:
                current = current.next
            current.next = new_node
        return head
