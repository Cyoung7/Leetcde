#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 8_429. N-ary Tree Level Order Traversal.py
@time: 2025/4/14 下午5:32
@desc:
"""
from collections import deque
from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        BFS层次遍历，N叉树和二叉树的唯一区别就是循环遍历儿子节点，而不止有左右节点
        :param root:
        :return:
        """
        queue = deque()
        value = list()
        if root:
            queue.append(root)

        while queue:
            level = list()
            for i in range(len(queue)):
                tmp_node = queue.popleft()
                level.append(tmp_node.val)
                if tmp_node.children:
                    for n in tmp_node.children:
                        queue.append(n)
            value.append(level)
        return value

