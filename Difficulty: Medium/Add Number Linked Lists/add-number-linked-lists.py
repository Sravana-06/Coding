class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addTwoLists(self, head1, head2):
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        h1 = reverse(head1)
        h2 = reverse(head2)

        carry = 0
        dummy = Node(0)
        curr = dummy

        while h1 or h2 or carry:
            s = carry
            if h1:
                s += h1.data
                h1 = h1.next
            if h2:
                s += h2.data
                h2 = h2.next

            carry = s // 10
            curr.next = Node(s % 10)
            curr = curr.next

        result = reverse(dummy.next)

        while result and result.data == 0 and result.next:
            result = result.next

        return result
