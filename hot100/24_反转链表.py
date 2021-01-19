# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        current = head
        pre = None
        pnext = None

        while current is not None:
            pnext = current.next
            current.next = pre
            pre = current
            current = pnext

        return pre



