# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

""" K个一组翻转链表 """

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
    def reverseKGroup(self, head: Optional[ListNode], k):
        n = 0
        cur = head
        while cur:  # 求出链表长度
            n += 1
            cur = cur.next

        dummy = ListNode(next=head)
        p0 = dummy
        pre = None
        cur = p0.next
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next  # 提前创建一个临时变量nxt=p0.next
            p0.next.next = cur  # 把p0更新为下一段要翻转的链表的上一个节点
            p0.next = pre
            p0 = nxt  # 最后更新p0=nxt开启下一轮循环

        return dummy.next


if __name__ == '__main__':
    _head = [1, 2, 3, 4, 5]
    _k = 3

    _linked_head = create_list(_head)

    print_list(_linked_head)

    _solution = Solution()
    _res = _solution.reverseKGroup(head=_linked_head, k=_k)  # 这种方法不需要额外的存储空间, 因为链表的反转是通过逐个更改指针完成的, 是一个in-place操作
    print_list(_res)
