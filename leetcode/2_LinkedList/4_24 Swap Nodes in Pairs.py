#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 4_24 Swap Nodes in Pairs.py
@time: 2025/4/2 下午6:06
@desc:
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

    def printList(self):
        values = list()
        tmp_node = self.head
        while tmp_node.next is not None:
            values.append(tmp_node.next.val)
            tmp_node = tmp_node.next
        print(values)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        new_head = None
        node = head
        while node and node.next:
            if new_head is None:
                new_head = node.next
            tmp_node = node.next.next
            # 注意把交换的两个节点和之前接上
            if pre:
                pre.next = node.next
            # 交换
            node.next.next = node
            node.next = tmp_node
            # 记录下一轮的前节点
            pre = node
            # 往后移动两个节点
            node = tmp_node


        if new_head is None:
            new_head = head
        return new_head


if __name__ == '__main__':
    obj = MyLinkedList2()
    obj.addAtHead(6)
    obj.addAtHead(5)
    obj.addAtHead(4)
    obj.addAtHead(3)
    obj.addAtHead(2)
    obj.addAtHead(1)
    obj.printList()
    obj.head.next = Solution().swapPairs(obj.head.next)
    obj.printList()
