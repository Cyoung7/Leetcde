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
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head is not None and head.val == val:
            head = head.next

        # 加上虚拟表头，不用单独处理表头的特殊情况
        dummy_head = ListNode(0, head)

        pre = dummy_head
        tmp_node = dummy_head.next
        while tmp_node:
            if tmp_node.val == val:
                pre.next = tmp_node.next
                tmp_node = tmp_node.next
            else:
                pre = tmp_node
                tmp_node = tmp_node.next

        return dummy_head.next


if __name__ == '__main__':
    s = Solution()
