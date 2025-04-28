#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 2_707 Design Linked List.py
@time: 2025/4/1 下午4:03
@desc:
"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    """
    完全自己凭感觉实现，比较乱
    """
    def __init__(self):
        self.head = ListNode()
        self.tail = None

    def get(self, index: int) -> int:
        tmp_node = self.head.next
        while index > 0:
            if tmp_node.next is not None:
                tmp_node = tmp_node.next
            else:
                return -1
            index -= 1
        if tmp_node:
            return tmp_node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node
        if self.tail is None:
            self.tail = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val, None)
        if self.tail is None:
            self.addAtHead(val)
        else:
            self.tail.next = node
            self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        pre = self.head
        tmp_node = self.head.next
        while index > 0 and tmp_node:
            if tmp_node.next is not None:
                pre = tmp_node
                tmp_node = tmp_node.next
                index -= 1
            else:
                break

        if index == 0:
            node = ListNode(val, tmp_node)
            pre.next = node

        elif index == 1 and tmp_node:
            node = ListNode(val, None)
            tmp_node.next = node
            self.tail = node
        else:
            pass

    def deleteAtIndex(self, index: int) -> None:
        pre = self.head
        tmp_node = self.head.next
        while index > 0:
            if tmp_node.next is not None:
                pre = tmp_node
                tmp_node = tmp_node.next
                index -= 1
            else:
                break

        if index == 0 and self.head.next is not None:
            pre.next = tmp_node.next
            if self.tail is tmp_node:
                self.tail = pre
        else:
            pass

    def printList(self):
        values = list()
        tmp_node = self.head
        while tmp_node.next is not None:
            values.append(tmp_node.next.val)
            tmp_node = tmp_node.next
        print(values)


class MyLinkedList2:
    """
    教学思路,加了虚拟的head，统一节点的访问方式
    """
    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if self.size < index or index < 0:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        node = ListNode(val, None)
        cur.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        cur = self.head
        for i in range(index):
            cur = cur.next
        node = ListNode(val, cur.next)
        cur.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or self.head.next is None:
            return
        cur = self.head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1


if __name__ == '__main__':
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    obj.addAtHead(1)
    # obj.addzzj.get(1))
    obj.printList()
    # print(obj.get(3))
    # obj.deleteAtIndex(3)
    # obj.deleteAtIndex(0)
    # print(obj.get(0))
    # obj.deleteAtIndex(0)
    # print(obj.get(0))

    # obj.addAtHead(2)
    # obj.addAtHead(7)
    # obj.addAtHead(3)
    # obj.addAtHead(6)
    # obj.addAtTail(4)



    # obj.deleteAtIndex(2)
    # obj.printList()
    # obj.addAtTail(3)
    # obj.addAtIndex(1, 2)
    # print(obj.get(1))
    # obj.deleteAtIndex(1)
    # obj.printList()
    # print(obj.get(1))
