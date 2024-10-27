# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(node: Optional[ListNode]):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print()


def create_list(elements: List):
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow

        return None


if __name__ == '__main__':
    _head = [3, 2, 0, -4]
    _linked_head = create_list(_head)
    print(_linked_head)

    _solution = Solution()
    _res = _solution.detectCycle(head=_linked_head)
    print(_res)
