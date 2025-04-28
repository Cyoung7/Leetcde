#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 5_19 Remove Nth Node From End of List.py
@time: 2025/4/2 下午6:39
@desc:
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        朴素解法，扫描两遍
        :param head:
        :param n:
        :return:
        """
        if head is None:
            return None
        # 算链表的长度
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # 删除节点的正向索引，0开始计算
        rm_idx = length - n
        node = head
        pre = None
        for i in range(rm_idx):
            pre = node
            node = node.next
        # 删除中间节点
        if pre is not None:
            pre.next = node.next
            return head
        # 删除首节点
        else:
            return head.next


class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        进阶解法：快慢指针，扫描一遍
        但是提交的用时更多....
        :param head:
        :param n:
        :return:
        """
        if head is None:
            return None

        fast_node = head
        slow_node = head
        pre = None
        mv_n = 0
        while fast_node:
            fast_node = fast_node.next
            mv_n += 1
            # 快指针先移动n步之后，慢指针开始移动
            # 快指针移动到末尾，慢指针就是要删除的节点
            if mv_n > n:
                pre = slow_node
                slow_node = slow_node.next
        if pre:
            pre.next = slow_node.next
            return head
        else:
            return head.next
