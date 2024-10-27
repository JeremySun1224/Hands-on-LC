# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from typing import List


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_link(elements: List) -> Node:
    head = Node(val=elements[0])
    current = head
    for element in elements[1:]:
        current.next = Node(element)
        current = current.next
    return head  # 返回的head其实是一个node


def print_link(node: Node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print()


def reverse_list(head: Node) -> Node:
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


# def reverse_partial_list(head, left, right):
#     dummy = Node(next=head)
#     p0 = dummy
#     for _ in range(left - 1):
#         p0 = p0.next
#
#     pre = None
#     cur = p0.next
#     for _ in range(right - left + 1):
#         nxt = cur.next
#         cur.next = pre
#         pre = cur
#         cur = nxt
#
#     p0.next.next = cur
#     p0.next = pre
#
#     return dummy.next


def reverse_partial_list(head, left, right):
    dummy = Node(next=head)  # 创建值为0的虚拟头节点, next指针指向原链表的head
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
    _list = [1, 2, 3, 4, 5]
    _link = create_link(elements=_list)
    print_link(node=_link)

    # # 反转链表
    # _reverse_link = reverse_list(_link)
    # print_link(_reverse_link)

    # 反转部分链表
    _left, _right = 2, 4

    _reverse_partial_link = reverse_partial_list(head=_link, left=_left, right=_right)
    print(_reverse_partial_link)
