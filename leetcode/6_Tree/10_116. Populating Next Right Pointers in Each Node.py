#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 10_116. Populating Next Right Pointers in Each Node.py
@time: 2025/4/14 下午6:06
@desc:
"""
from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        BFS层次遍历，每一层的前一个节点的next指向后一个节点
        :param root:
        :return:
        """
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            level_len = len(queue)

            for i in range(0, level_len):
                tmp_node = queue.popleft()
                if i < (level_len-1):
                    tmp_node.next = queue[0]
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)

        return root
