#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_203.py
@time: 2025/4/1 下午3:43
@desc:
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    待完成：将链表相关题目，都用虚拟头处理，简化head的节点处理
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head is not None and head.val == val:
            head = head.next

        pre = head
        tmp_node = head.next if head is not None else None
        while tmp_node:
            if tmp_node.val == val:
                pre.next = tmp_node.next
                tmp_node = tmp_node.next
            else:
                pre = tmp_node
                tmp_node = tmp_node.next

        return head


if __name__ == '__main__':
    s = Solution()
