#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 13_226. Invert Binary Tree.py
@time: 2025/4/15 上午8:56
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        BFS
        :param root:
        :return:
        """
        queue = collections.deque()
        if root:
            queue.append(root)

        while queue:
            for _ in range(len(queue)):
                tmp_node = queue.pop()
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)
                tmp_node.left, tmp_node.right = tmp_node.right, tmp_node.left
        return root


class Solution1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        DFS，前序遍历，后序遍历都可以，只有中序遍历不行
        :param root:
        :return:
        """
        if root is None:
            return None
        # 前序遍历
        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
