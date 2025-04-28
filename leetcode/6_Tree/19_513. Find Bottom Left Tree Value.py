#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 19_513. Find Bottom Left Tree Value.py
@time: 2025/4/15 下午7:57
@desc:
"""
import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        bfs:找到最后一层的第一个值
        :param root:
        :return:
        """
        queue = collections.deque()
        if root:
            queue.append(root)
        first_value = 0
        while queue:
            first_value = 0
            for i in range(len(queue)):
                tmp_node = queue.popleft()
                if i == 0:
                    first_value = tmp_node.val
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)
        return first_value


class Solution1:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        dfs:找到最后一层的第一个值
        :param root:
        :return:
        """
        max_depth = -1
        first_value = 0

        def dfs(node: Optional[TreeNode], depth) -> None:
            nonlocal max_depth, first_value
            if node is None:
                return
            if node.left is None and node.right is None:
                if depth > max_depth:
                    max_depth = depth
                    first_value = node.val
                    return
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
            return
        dfs(root, 0)
        return first_value

