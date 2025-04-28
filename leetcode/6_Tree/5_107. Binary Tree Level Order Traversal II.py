#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 5_107. Binary Tree Level Order Traversal II.py
@time: 2025/4/14 下午5:14
@desc:
"""
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        偷鸡做法，正向层次遍历，最后颠倒结果
        :param root:
        :return:
        """
        queue = deque()
        value = list()
        if root:
            queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                tmp_node = queue.popleft()
                level.append(tmp_node.val)
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)
            value.append(level)
        return value[::-1]
