# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from typing import Optional, List


class ListNode(object):
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
    def reverseBetween(self, head: Optional[ListNode], left, right) -> Optional[ListNode]:
        dummy = ListNode(next=head)  # 创建值为0的虚拟头节点, next指针指向原链表的head
        p0 = dummy
        for _ in range(left - 1):  # 找到第一个节点
            p0 = p0.next

        pre = None
        cur = p0.next
        for _ in range(right - left + 1):  # 找到最后一个节点
            nxt = cur.next  # 暂存当前节点的下一个节点
            cur.next = pre  # 反转当前节点的指针, 使其指向pre
            pre = cur
            cur = nxt

        p0.next.next = cur  # 重新链接反转后的子链表
        p0.next = pre

        return dummy.next


if __name__ == '__main__':
    _head = [1, 2, 3, 4, 5]
    _left = 2
    _right = 4

    _linked_head = create_list(elements=_head)
    print_list(_linked_head)

    _solution = Solution()
    _res = _solution.reverseBetween(head=_linked_head, left=_left, right=_right)
    print_list(_res)
