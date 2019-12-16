# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """判断链表是否有环"""
        a = b = head
        try:
            while True:
                a = a.next
                b = b.next.next
                if a == b:
                    if a.next:
                        return True
        except Exception:
            return False
