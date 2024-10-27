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
    def reorderList(self, head: Optional[ListNode]):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        mid = self.middleNode(head=head)
        head2 = self.reverseList(mid)
        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 = nxt2

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None  # 记录当前节点的前一个节点
        cur = head  # 将当前节点赋值为头节点, 用于遍历链表
        while cur:  # 当cur为空时, 表示遍历到链表末尾
            nxt = cur.next  # 在更改当前cur的next指针之前, 需要先保存下一个节点的引用, 记作nxt
            cur.next = pre  # 将当前节点cur的next指针指向下一个节点pre, 实现反转
            pre = cur  # 将pre更新为当前节点cur, 为下一次迭代做准备
            cur = nxt  # 将cur更新为下一个节点nxt, 继续遍历链表

        return pre


if __name__ == '__main__':
    _head = [1, 2, 3, 4, 5]
    _linked_head = create_list(_head)
    print_list(_linked_head)

    _solution = Solution()
    _solution.reorderList(head=_linked_head)
    print_list(_linked_head)
