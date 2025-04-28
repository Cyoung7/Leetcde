#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 11_104. Maximum Depth of Binary Tree.py
@time: 2025/4/14 下午6:37
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        BFS层次遍历
        :param root:
        :return:
        """
        queue = collections.deque()
        if root:
            queue.append(root)
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                tmp_node = queue.popleft()
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)
        return depth


class Solution1:
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.getHeight(root.left)
        right_depth = self.getHeight(root.right)
        return max(left_depth, right_depth) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        DFS，求高度，后序遍历
        :param root:
        :return:
        """
        return self.getHeight(root)


class Solution2:
    result = -1

    def getDepth(self, root: Optional[TreeNode], depth) -> None:
        if root is None:
            self.result = max(self.result, depth-1)
            return None
        self.getDepth(root.left, depth + 1)
        self.getDepth(root.right, depth + 1)
        return None

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        DFS，求深度，前序遍历
        :param root:
        :return:
        """
        self.getDepth(root, 1)
        return self.result
