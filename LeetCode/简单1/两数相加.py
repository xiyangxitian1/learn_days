# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """

        :param l1:
        :param l2:
        :return:
        """
        head0 = ListNode(0)
        head = head0
        jin = 0
        while l1 and l2:
            val = l1.val + l2.val + jin
            if val > 9:
                jin = 1
                val -= 10
            else:
                jin = 0
            node = ListNode(val)
            head.next = node
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + jin
            if val > 9:
                jin = 1
                val -= 10
            else:
                jin = 0
            node = ListNode(val)
            head.next = node
            head = head.next
            l1 = l1.next

        while l2:
            val = l2.val + jin
            if val > 9:
                jin = 1
                val -= 10
            else:
                jin = 0
            node = ListNode(val)
            head.next = node
            head = head.next
            l2 = l2.next

        if jin:
            head.next = ListNode(1)

        return head0.next
