# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

""" 单向链表 """


class Node:
    def __init__(self, data):
        self.data = data  # 节点数据
        self.next = None  # 指向下一个节点的引用


class LinkedList:
    def __init__(self):
        self.head = None  # 初始化链表的头节点为空

    def append(self, data):
        new_node = Node(data=data)  # 创建新节点
        if self.head is None:  # 如果链表为空, 则把新节点设为头节点
            self.head = new_node
            return
        last = self.head
        while last.next:  # 遍历找到链表的末尾, 以将新节点链接到链表末尾
            last = last.next
        last.next = new_node  # 将新节点链接到链表末尾

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


if __name__ == '__main__':
    _linked_list = LinkedList()
    _linked_list.append(1)
    _linked_list.append(2)
    _linked_list.append(3)
    _linked_list.append(4)
    _linked_list.display()

    _linked_list.prepend(0)
    _linked_list.display()
