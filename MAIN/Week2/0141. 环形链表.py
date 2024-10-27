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


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:  # 如果快慢指针相遇
                return True
        return False


if __name__ == '__main__':
    _head = [1, 2, 3, 4, 5]
    _linked_head = create_list(elements=_head)
    print_list(_linked_head)

    _solution = Solution()
    _res = _solution.hasCycle(head=_linked_head)
    print(_res)

    """
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
